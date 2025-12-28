import psutil

def cpu_threshold():

    get_cpu = int(input("please enter the CPU thershold"))
    cpu_usage = psutil.cpu_percent(interval=1)

    if get_cpu > cpu_usage:
        print ("good to go")
    else:
        print ("Alert mail sent!")

cpu_threshold()

# import psutil

# get_cpu = input("please enter the CPU thershold")
# cpu_usage = psutil.cpu_percent(interval=1)
# print (cpu_usage)
# if get_cpu < cpu_usage:
#     print ("good to go")
# else:
#     print("Alert email sent")