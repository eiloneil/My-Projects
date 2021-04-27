
# import keyboard as kb
# import matplotlib.pyplot as plt
    # TO INSTALL the above libraries go to the CMD and type "pip install matplotlib" or "pip install keyborad", 
    # IF NOT WORKING: Type on the CMD: "py -m pip install matplotlib"

from datetime import datetime
import time



qst_num = int(input('How many questions are there?: '))
qst_list = list(range(1,qst_num+1))

qst_dict = {}
for q in qst_list:
    qst_dict[q] = 0

qst = 1
last_time = datetime.now()
start_time = last_time
skipped = []
done_qst = []


def next_qst(done, skp, all_qst, qst):
    available_q = []
    next_skp = []
    passed_skp = []
    for s in skp:
        if s > qst:
            next_skp.append(s)
        else:
            passed_skp.append(s)
    for q in all_qst:
        if (q not in done) and (q not in skp):
            available_q.append(q)
    
    if len(available_q) == 0 and (len(skp) > 0):
        if qst < skp[-1]:
            return next_skp[0]
        else:
            return passed_skp[0]
    elif len(available_q) == 0:
        return all_qst[-1] + 1
    
    else:
        return available_q[0]
        
        
        


def get_diff(lasttime):
    now = datetime.now()
    diff_seconds = int((now-lasttime).total_seconds())
    minutes = str(diff_seconds // 60)
    seconds = str(diff_seconds % 60)
    diff = minutes.zfill(2) + ':' + seconds.zfill(2)
    return [diff, diff_seconds]


def stop(lasttime, qst_p, st):
    now = datetime.now()
    diff_func = get_diff(lasttime)
    diff = diff_func[0]
    diff_sec = diff_func[1]
    total_diff = get_diff(st)[0]
    print('Question:',qst_p, '\tTime:', diff, '\tTotal Time:', total_diff)
    return [now, diff_sec]


def f_complete(last_time_param, qst_param, start_time_param):
#     time.sleep(0.2)
    global skipped
    global qst_dict
    global done_qst
    global qst_list
    
    if qst_param in skipped:
        print('---Returned To question', qst_param, '---')
    else:
        print('---Completed question', qst_param, '---')
        
    stop_output = stop(last_time_param, qst_param, start_time_param)
    last_time_param = stop_output[0]
    qst_dict[qst_param] +=  stop_output[1]
    print('----------------------------')
    
    if qst_param in skipped:        
        skipped.remove(qst_param)
        
    done_qst.append(qst_param)
    qst_param = next_qst(done_qst, skipped, qst_list, qst_param)
    if qst_param <= qst_list[-1]:
        print('Working on Question number',qst_param)
    output = {'last_time': last_time_param, 'qst': qst_param}
    return output


def f_skip(last_time_param, qst_param, start_time_param):
#     time.sleep(0.2)
    global skipped
    global qst_dict
    global qst_list
    global done_qst
    
    print('---Skip---')
    stop_output_param = stop(last_time_param, qst_param, start_time_param)
    last_time_param = stop_output_param[0]
    qst_dict[qst_param] += stop_output_param[1]
    print('----------')
    if qst_param not in skipped:
        skipped.append(qst_param)
    qst_param = next_qst(done_qst, skipped, qst_list, qst_param)
    if qst_param <= qst_list[-1]:
        print('Working on Question number',qst_param)
    output = {'last_time': last_time_param, 'qst': qst_param}
    return output


def f_back():
    global skipped
    
    print('Skipped Questions:', skipped)
    back_to_qst = int(input('To which question do you want to go back?:  '))
    last_time = datetime.now()
    qst_param = back_to_qst
    print('Working on Question number',qst_param)
    return qst_param



print('Working on Question number 1')

while len(done_qst) < qst_num:
    action = input('** Press [Enter] to Complete,   [s] to Skip,   [b] to Go Back,   [k] to End: >> ')
    print()
    
    if action == '':
        complete = f_complete(last_time, qst, start_time)
        last_time = complete['last_time']
        qst = complete['qst']

#         else:
#             qst += 1
        
    if action == 's':
        skip = f_skip(last_time, qst, start_time)
        last_time = skip['last_time']
        qst = skip['qst']
        
    if action == 'b':
        qst = f_back()
        
    if action == 'k':
        print('Break')
        break
    if len(done_qst) == len(qst_list):
        print('You are Done!')
        break
total_time = get_diff(start_time)[0]

print('\nStopped at', datetime.now().strftime("%H:%M:%S"),'\nTotal Time:', total_time)

print()
print('Final Stats:\n-------------------')
for q in qst_list:
    print('Question #', q, '\tTotal Time:', str(qst_dict[q] // 60).zfill(2)+':'+str(qst_dict[q] % 60).zfill(2))

    
    
    # After installing matplotlib
    
#x = list(qst_dict.keys())
#y = list(qst_dict.values())
#
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax.bar(x, y)
#plt.show()    

delay = input('\nPress [Enter] to Exit')
