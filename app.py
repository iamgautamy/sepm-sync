from flask import Flask,jsonify
import cpuinfo
import GPUtil
import psutil
import math
import shutil


#CPU INPUT
cpu_og = str(cpuinfo.get_cpu_info()['brand_raw'])
cpu_og = cpu_og.split(' ')
cpu_og = cpu_og[1:4]
string2=str("")
for i in cpu_og:
   string2=string2+i+" "
#print(string2)


#GPU INPUT
gpu_og = GPUtil.getGPUs()
for gpu in gpu_og:
    gpu_name = gpu.name
    #print(gpu_name)


def get_size(bytes, suffix="B"):

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor


#RAM INPUT
svmem = psutil.virtual_memory()
ram_og = get_size(svmem.total)
#print(ram_og)
get_ram_int = ram_og.split(' ')
get_ram_int = float(get_ram_int[0])
get_ram_int = math.ceil(get_ram_int)
#print(get_ram_int)


#HDD INPUT
total, used, free = shutil.disk_usage("/")
hdd_og = int(free // (2**30))
#print(hdd_og)



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'cpum':string2,'ramm':get_ram_int,'hddm':hdd_og,'gpum':gpu_name})




if __name__ == "__main__":
    app.run(debug=True)
