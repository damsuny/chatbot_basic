from flask import Flask, request
app = Flask(__name__)

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', method=['POST'])
def sayHello():
	body = request.get_json()                               # 봇 시스템 요청 body(SkillPayload)
	print(body)                                             # SkillPayload 출력

	responseBody = {
		"version" : "2.0",
		"template" : {
			"outputs" : [
				{
					"simpleText" : {
						"text" : "안녕 hello I'm Ryan"
					}
				}
			]
		}
	}

	return responseBody

# 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
	body = request.get_json()                               # 봇 시스템 요청 body(SkillPayload)
	print(body)                                             # SkillPayload 출력

	responseBody = {
		"version" : "2.0",
		"template" : {
			"outputs" : [
				{
					"simpleImage" : {
						"imageUrl" : "https://t1.daum.net/friends/prod/category/M001_friends_ryan2.jpg",
						"altText" : "hello I'm Ryan"
					}
				}
			]
		}
	}

	return responseBody

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)