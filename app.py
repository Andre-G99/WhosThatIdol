import os
import face_recognition

from flask import Flask, request, render_template
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.static_folder = 'static'
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=10,
    DROPZONE_MAX_FILES=1,
    DROPZONE_UPLOAD_MULTIPLE=False,
    REDIRECT_URL='results<result>'
)
dropzone = Dropzone(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # save the photo
        file = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], file.filename)
        file.save(file_path)

        # call detect_face_in_image() to compare uploaded image to known faces
        result_raw = detect_face_in_image(file)
        result = str(result_raw).strip("[]")
        missing_one_quote = result.replace("'", "")
        missing_one_quote.replace("'", "")

        if result_raw == ["Could Not Find Group", "No Match"]:
            # write results to txt file
            result_file = open("result.txt", "w")
            result_file.writelines(result_raw[1])
            result_file.writelines("\n" + result_raw[0])

        elif result_raw == ["Could Not Pinpoint. Try a different picture.", "Multiple Matches."]:
            # write results to txt file
            result_file = open("result.txt", "w")
            result_file.writelines(result_raw[1])
            result_file.writelines("\n" + result_raw[0])


        elif len(result_raw) == 1:
            print(result_raw)
            group_name, idol_name = missing_one_quote.split(',')
            result_file = open("result.txt", "w")
            result_file.writelines(idol_name)
            result_file.writelines("\n" + group_name)

        elif len(result_raw) == 2 and result_raw != ["Could Not Find Group", "No Match"] and result_raw != ["Error", "No Face Found"]:
            print(result_raw)
            get_rid_of_bracket1 = missing_one_quote.replace("]", "")
            get_rid_of_bracket2 = get_rid_of_bracket1.replace("[", "")
            print(get_rid_of_bracket2)
            group_name1, idol_name1, group_name2, idol_name2 = get_rid_of_bracket2.split(',')
            # write results to txt file
            result_file = open("result.txt", "w")
            result_file.writelines(idol_name1)
            result_file.writelines("\n" + group_name1)
            result_file.writelines("\n," + idol_name2)
            result_file.writelines("\n," + group_name2)

        else:
            print("couldnt find face")
            result_file = open("result.txt", "w")
            result_file.writelines(result_raw[1])
            result_file.writelines("\n" + result_raw[0])

        return result
    else:
        return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def print_match():
    file = open("result.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    if line_count <= 2:
        # set final_match to txt in result.txt
        idol_name = open('result.txt', mode='r').readline()
        group_name = open('result.txt', mode='r').readlines()[1]
        return render_template('results.html', idol1=idol_name, group1=group_name)

    elif line_count > 2:
        idol_name = open('result.txt', mode='r').readline()
        group_name = open('result.txt', mode='r').readlines()[1]
        idol_name2 = open('result.txt', mode='r').readlines()[2]
        group_name2 = open('result.txt', mode='r').readlines()[3]
        # send result text to html template
        return render_template('results.html', idol1=idol_name, group1=group_name, idol2=idol_name2, group2=group_name2)


def detect_face_in_image(image):
    # misc delacres
    match_list = []
    match_list2 = []
    groups_round_2 = []
    groups_round_3 = []

    # Weeekly Declares
    jiyoon_encoding = None
    jyoon_img = face_recognition.load_image_file("static/img/Weeekly/jiyoon.jpg")

    soeun_encoding = None
    soeun_img = face_recognition.load_image_file("static/img/Weeekly/soeun.jpg")

    soojin_encoding = None
    soojin_img = face_recognition.load_image_file("static/img/Weeekly/soojin.jpeg")

    monday_encoding = None
    monday_img = face_recognition.load_image_file("static/img/Weeekly/monday.jpg")

    jaehee_encoding = None
    jaehee_img = face_recognition.load_image_file("static/img/Weeekly/jaehee.jpg")

    jihan_encoding = None
    jihan_img = face_recognition.load_image_file("static/img/Weeekly/jihan.jpg")

    zoa_encoding = None
    zoa_img = face_recognition.load_image_file("static/img/Weeekly/zoa.jpg")

    # EXID Declares
    hani_encoding = None
    hani_img = face_recognition.load_image_file("static/img/EXID/hani.jpg")

    solji_encoding = None
    solji_img = face_recognition.load_image_file("static/img/EXID/solji.jpg")

    LE_encoding = None
    LE_img = face_recognition.load_image_file("static/img/EXID/LE.jpeg")

    hyerin_encoding = None
    hyerin_img = face_recognition.load_image_file("static/img/EXID/hyerin.jpg")

    jeonghwa_encoding = None
    jeonghwa_img = face_recognition.load_image_file("static/img/EXID/jeonghwa.jpg")

    # Twice Declares
    chaeyoung_encoding = None
    chaeyoung_img = face_recognition.load_image_file("static/img/Twice/chaeyoung.jpg")

    dahyun_encoding = None
    dahyun_img = face_recognition.load_image_file("static/img/Twice/dahyun.jpg")

    jeongyeon_encoding = None
    jeongyeon_img = face_recognition.load_image_file("static/img/Twice/jeongyeon.jpg")

    jihyo_encoding = None
    jihyo_img = face_recognition.load_image_file("static/img/Twice/jihyo.jpg")

    mina_encoding = None
    mina_img = face_recognition.load_image_file("static/img/Twice/mina.jpg")

    momo_encoding = None
    momo_img = face_recognition.load_image_file("static/img/Twice/momo.jpg")

    nayeon_encoding = None
    nayeon_img = face_recognition.load_image_file("static/img/Twice/nayeon.jpg")

    sana_encoding = None
    sana_img = face_recognition.load_image_file("static/img/Twice/sana.jpg")

    tzuyu_encoding = None
    tzuyu_img = face_recognition.load_image_file("static/img/Twice/tzuyu.jpg")

    # GIDLE Declares
    minnie_encoding = None
    minnie_img = face_recognition.load_image_file("static/img/gidle/minnie.jpg")

    miyeon_encoding = None
    miyeon_img = face_recognition.load_image_file("static/img/gidle/miyeon.jpeg")

    shuhua_encoding = None
    shuhua_img = face_recognition.load_image_file("static/img/gidle/shuhua.jpg")

    soojin_gidle_encoding = None
    soojin_gidle_img = face_recognition.load_image_file("static/img/gidle/soojin.jpg")

    soyeon_encoding = None
    soyeon_img = face_recognition.load_image_file("static/img/gidle/soyeon.jpeg")

    yuqi_encoding = None
    yuqi_img = face_recognition.load_image_file("static/img/gidle/yuqi.jpg")

    # BTS Declares
    hoseok_encoding = None
    hoseok_img = face_recognition.load_image_file("static/img/BTS/hoseok.jpg")

    jimin_bts_encoding = None
    jimin_bts_img = face_recognition.load_image_file("static/img/BTS/jimin.jpg")

    jin_encoding = None
    jin_img = face_recognition.load_image_file("static/img/BTS/jin.jpg")

    jungkook_encoding = None
    jungkook_img = face_recognition.load_image_file("static/img/BTS/jungkook.jpg")

    namjoon_encoding = None
    namjoon_img = face_recognition.load_image_file("static/img/BTS/namjoon.jpg")

    taehyung_encoding = None
    taehyung_img = face_recognition.load_image_file("static/img/BTS/taehyung.jpg")

    yoongi_encoding = None
    yoongi_img = face_recognition.load_image_file("static/img/BTS/yoongi.jpg")

    # User Upload
    unknown_image = face_recognition.load_image_file(image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)

    try:
        # Weeekly
        jiyoon_encoding = face_recognition.face_encodings(jyoon_img)[0]
        soeun_encoding = face_recognition.face_encodings(soeun_img)[0]
        soojin_encoding = face_recognition.face_encodings(soojin_img)[0]
        monday_encoding = face_recognition.face_encodings(monday_img)[0]
        jaehee_encoding = face_recognition.face_encodings(jaehee_img)[0]
        jihan_encoding = face_recognition.face_encodings(jihan_img)[0]
        zoa_encoding = face_recognition.face_encodings(zoa_img)[0]

        # EXID
        hani_encoding = face_recognition.face_encodings(hani_img)[0]
        solji_encoding = face_recognition.face_encodings(solji_img)[0]
        LE_encoding = face_recognition.face_encodings(LE_img)[0]
        hyerin_encoding = face_recognition.face_encodings(hyerin_img)[0]
        jeonghwa_encoding = face_recognition.face_encodings(jeonghwa_img)[0]

        # Twice
        chaeyoung_encoding = face_recognition.face_encodings(chaeyoung_img)[0]
        dahyun_encoding = face_recognition.face_encodings(dahyun_img)[0]
        jeongyeon_encoding = face_recognition.face_encodings(jeongyeon_img)[0]
        jihyo_encoding = face_recognition.face_encodings(jihyo_img)[0]
        mina_encoding = face_recognition.face_encodings(mina_img)[0]
        momo_encoding = face_recognition.face_encodings(momo_img)[0]
        nayeon_encoding = face_recognition.face_encodings(nayeon_img)[0]
        sana_encoding = face_recognition.face_encodings(sana_img)[0]
        tzuyu_encoding = face_recognition.face_encodings(tzuyu_img)[0]

        # GIDLE
        minnie_encoding = face_recognition.face_encodings(minnie_img)[0]
        miyeon_encoding = face_recognition.face_encodings(miyeon_img)[0]
        shuhua_encoding = face_recognition.face_encodings(shuhua_img)[0]
        soojin_gidle_encoding = face_recognition.face_encodings(soojin_gidle_img)[0]
        soyeon_encoding = face_recognition.face_encodings(soyeon_img)[0]
        yuqi_encoding = face_recognition.face_encodings(yuqi_img)[0]

        # BTS
        hoseok_encoding = face_recognition.face_encodings(hoseok_img)[0]
        jimin_bts_encoding = face_recognition.face_encodings(jimin_bts_img)[0]
        jin_encoding = face_recognition.face_encodings(jin_img)[0]
        jungkook_encoding = face_recognition.face_encodings(jungkook_img)[0]
        namjoon_encoding = face_recognition.face_encodings(namjoon_img)[0]
        taehyung_encoding = face_recognition.face_encodings(taehyung_img)[0]
        yoongi_encoding = face_recognition.face_encodings(yoongi_img)[0]

    except:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [

        # Weeekly
        jiyoon_encoding,
        soeun_encoding,
        soojin_encoding,
        monday_encoding,
        jaehee_encoding,
        jihan_encoding,
        zoa_encoding,

        # EXID
        hani_encoding,
        solji_encoding,
        LE_encoding,
        hyerin_encoding,
        jeonghwa_encoding,

        # Twice
        chaeyoung_encoding,
        dahyun_encoding,
        jeongyeon_encoding,
        jihyo_encoding,
        mina_encoding,
        momo_encoding,
        nayeon_encoding,
        sana_encoding,
        tzuyu_encoding,

        # GIDLE
        minnie_encoding,
        miyeon_encoding,
        shuhua_encoding,
        soojin_gidle_encoding,
        soyeon_encoding,
        yuqi_encoding,

        # BTS
        hoseok_encoding,
        jimin_bts_encoding,
        jin_encoding,
        jungkook_encoding,
        namjoon_encoding,
        taehyung_encoding,
        yoongi_encoding
    ]

    group_and_name = [
        # Weeekly
        ["Weeekly", "Shin Jiyoon"],
        ["Weeekly", "Park Soeun"],
        ["Weeekly", "Lee Soojin"],
        ["Weeekly", "Kim Ji Min aka Monday"],
        ["Weeekly", "Lee Jaehee"],
        ["Weeekly", "Han Jihyo aka Jihan"],
        ["Weeekly", "Jo Hyewon aka Zoa"],

        # EXID
        ["EXID", "Ahn HeeYeon aka Hani"],
        ["EXID", "Heo Solji"],
        ["EXID", "Ahn Hyojin aka LE"],
        ["EXID", "Seo Hyerin"],
        ["EXID", "Park Jeonghwa"],

        # Twice
        ["Twice", "Son Chaeyoung"],
        ["Twice", "Kim Da Hyun"],
        ["Twice", "Yoo Jeongyeon"],
        ["Twice", "Park Jihyo"],
        ["Twice", "Myoui Mina"],
        ["Twice", "Hirai Momo"],
        ["Twice", "Im Nayeon"],
        ["Twice", "Minatozaki Sana"],
        ["Twice", "Chou Tzuyu"],

        # GIDLE
        ["(G)I-DLE", "Nicha Yontararak / Kim Minhee(Korean Name) aka Minnie"],
        ["(G)I-DLE", "Cho Miyeon"],
        ["(G)I-DLE", "Yeh Shuhua / Yoo Suhwa(Korean Name) aka Shuhua"],
        ["(G)I-DLE", "Seo Soojin"],
        ["(G)I-DLE", "Jeon Soyeon"],
        ["(G)I-DLE", "Song Yuqi / Song Woogi aka Yuqi"],

        # BTS
        ["BTS", " Jung Hoseok aka J-Hope"],
        ["BTS", "Park Jimin"],
        ["BTS", "Kim Seokjin"],
        ["BTS", "Jeon Jungkook"],
        ["BTS", "Kim Namjoon aka RM"],
        ["BTS", "Kim Taehyung aka V"],
        ["BTS", "Min Yoongi aka Suga"]
    ]

    if len(unknown_encoding) > 0:
        match_result = face_recognition.compare_faces(known_faces, unknown_encoding[0], tolerance=0.39)

        print(match_result)

        if not any(match_result):
            print("no matches")
            return ["Could Not Find Group", "No Match"]

        else:
            for x in range(0, len(match_result)):
                if match_result[x]:
                    match_list.append(known_faces[x])
                    groups_round_2.append(group_and_name[x])

            if len(groups_round_2) == 1:
                print("default")
                return groups_round_2

            elif len(groups_round_2) == 2:
                return groups_round_2

            elif len(groups_round_2) > 2:
                match_result2 = face_recognition.compare_faces(match_list, unknown_encoding[0], tolerance= 0.37)
                print("Test1")
                print(groups_round_2)
                for x in range(0, len(match_result2)):
                    if match_result2[x]:
                        match_list2.append(match_list[x])
                        groups_round_3.append([groups_round_2[x]])

                if len(groups_round_3) <= 2:
                    print("NARROWED")
                    print(groups_round_3)

                elif groups_round_3 > 2:
                    return ["Could Not Pinpoint. Try a different picture.", "Multiple Matches."]

                print("default for narrow")
                return groups_round_3
            else:
                print("something wrong")
    else:
        return ["Error", "No Face Found"]

if __name__ == '__main__':
    app.run(debug=True)
