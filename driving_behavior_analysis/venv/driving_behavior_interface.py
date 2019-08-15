from  flask import  Flask, Response
from gevent.pywsgi import WSGIServer
import time
from gevent import  monkey
import  os
import  base64
import json
from vechile_analysis import  start_analysis
import  concurrent
#to buid the recmd algorithm model once time
ENCODING='utf-8'
monkey.patch_all()
app=Flask(__name__)



@app.route('/start_vechile_analysis')
def start_vechile_analysis():
    try:
        start_analysis()
    except Exception as e:
        print("error is "+e)
        return "start error"
    return "finsh the action"

    # try:
    #     with ThreadPoolExecutor(max_workers=1) as executor:
    #         futures=executor.submit(main())
    #         print(futures)
    #         concurrent.futures.as_completed(futures)
    #         res=futures.result()
    #         print(res,futures)
    # except Exception as e:
    #     print("error is "+e)
    #     return "start error"

@app.route('/get_analysis_bar')
def get_pic():
    try:
        pic_list={}
        pic_list['content']='pic_bar'
        pic_list['encoding']='base64'
        files=os.listdir('./pic')
        for file in files:
            f=open('./pic/%s' %(file),'rb')
            file=file.split('.')[0]
            base64_bytes=base64.b64encode(f.read())
            base64_string=base64_bytes.decode(ENCODING)
            pic_list[file]=base64_string
    except Exception as e:
        print("error reason is :"+e)
        return 'error to get the bar'
    return  Response(json.dumps(pic_list),mimetype='application/json')


@app.route('/get_analysis_data')
def get_data():
    try:
        fileObject=open('./analysis_data/analysis_data.json','r')
        load_dict=json.load(fileObject)
        load_dict["content"]='analysis_data'
        load_dict["encoding"]='json'
        return Response(json.dumps(load_dict),mimetype='application/json')
    except Exception as e:
        print("error reason is :"+e)
        return 'error to get the data'



if __name__ == '__main__':
    app.debug=True
    http_server=WSGIServer(('0.0.0.0',7001),app)
    http_server.serve_forever()