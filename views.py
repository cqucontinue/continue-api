from flask import Flask, request, make_response, render_template
from pymongo import MongoClient
from xml.etree import ElementTree

# connect mongodb
conn = MongoClient("localhost", 27017)
db = conn.newmembers
coll = db.membersinfo

# open like.xml
tree = ElementTree.parse("like.xml")
like = tree.getroot()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
	csong = like.findall("work")[0].text
	sss = like.findall("work")[1].text
	pigeon = like.findall("work")[2].text
	wb = like.findall("work")[3].text
	return render_template("index.html", csong=csong, sss=sss, pigeon=pigeon, wb=wb)

@app.route("/contact_us", methods=["POST"])
def contact_us():
	if request.method == "POST":
		name = request.form.get("name")
		if coll.find({"name": name}):
			return make_response("repeatly")
		else:
			email = request.form.get("email")
			qqnumbers = request.form.get("qqnumbers")
			telephone = request.form.get("telephone")
			input_ideas = request.form.get("input_ideas")
			coll.save({"name": name, "email": email, "qqnumbers": qqnumbers, 
							"telephone": telephone, "input_ideas": input_ideas})
			return make_response("success")

@app.route("/agree", methods=["POST"])
def agree():
	if request.method == "POST":
		name = request.form.get("name")
		name_map = {"csong": 0, "sss": 1, "pigeon": 2, "wb": 3}
		agreenum = like.findall("work")[name_map[name]]
		agreenum.text = str(int(agreenum.text) + 1)
		tree.write("like.xml", encoding="utf-8", xml_declaration=True)
		return make_response(agreenum.text)

@app.route("/getinfo", methods=["GET"])
def getinfo():
	infos = []
	count = 1
	for newMemberInfo in coll.find():
		del newMemberInfo["_id"]
		newMemberInfo["index"] = count
		infos.append(newMemberInfo)
		count += 1
	return render_template("info.html", infos=infos)


if __name__ == '__main__':
	app.run()





