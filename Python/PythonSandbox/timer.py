from datetime import datetime
import keyboard as kb
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

print('Working on Question number 1')

while len(done_qst) < qst_num:
    
    if kb.is_pressed('space'):
        time.sleep(0.2)
        if qst in skipped:
            print('---Returned To question', qst, '---')
        stop_output = stop(last_time, qst, start_time)
        last_time = stop_output[0]
        qst_dict[qst] +=  stop_output[1]
        if qst in skipped:
            print('----------')
            skipped.remove(qst)
        done_qst.append(qst)
        qst = next_qst(done_qst, skipped, qst_list, qst)
        print('Working on Question number',qst)

#         else:
#             qst += 1
        
    if kb.is_pressed('s'):
        time.sleep(0.2)
        print('---Skip---')
        stop_output = stop(last_time, qst, start_time)
        last_time = stop_output[0]
        qst_dict[qst] +=  stop_output[1]
        print('----------')
        if qst not in skipped:
            skipped.append(qst)
#         if done_qst[-1] + 1 in skipped:
        qst = next_qst(done_qst, skipped, qst_list, qst)
        print('Working on Question number',qst)
        
    if kb.is_pressed('b'):
        time.sleep(0.2)
        print('Skipped Questions:', skipped)
        back_to_qst = int(input('To which question do you want to go back?:  '))
        last_time = datetime.now()
        qst = back_to_qst
        print('Working on Question number',qst)
    if kb.is_pressed('backspace'):
        print('Break')
        break
    if len(done_qst) == len(qst_list):
        print('You are Done!')
        break
total_time = get_diff(start_time)[0]
print('Stopped at', datetime.now().strftime("%H:%M:%S"),'\nTotal Time:', total_time)

print()
print('Final Stats:\n-------------------')
for q in qst_list:
    print('Question #', q, '\tTotal Time:', str(qst_dict[q] // 60).zfill(2)+':'+str(qst_dict[q] % 60).zfill(2))
    
    