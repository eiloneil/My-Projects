import streamlit as st

# Notes Converter!
### Set your notes to any key you want!

 

## Create Functions

all_notes = ['do', 'do#', 're', 're#', 'mi', 'fa', 'fa#', 'sol', 'sol#', 'la', 'la#', 'si']

def get_notes_dict():
    
    tone_to_note = {}
    note_to_tone = {}
    t = 0

    for note in all_notes:
        tone_to_note[t] = note
        note_to_tone[note] = t
        t = t + 0.5
    
    return tone_to_note, note_to_tone


tone_to_note, note_to_tone = get_notes_dict()


def final_converter(notes, key):
    notes_to_raise = get_diez(key[0], key[1])
    
    final = []
    for note in notes:
        
        new_note = convert(note, notes_to_raise)
        final.append(new_note)
    return final
        
        
def convert(n, k):
    if n in k.keys():
        n = k[n]
        
    return n



def find_notes_to_raise(k):
    if 'major' in k.lower():
        pass
       
        
def raise_note(n, t):
    
    n_ton = note_to_tone[n]
    n_ton = (n_ton + t)
    t_new = n_ton % 6
    
    return tone_to_note[t_new]



def get_diez(k, k_type):
    
    if k_type == 'major' and k != 'fa' and '#' not in k:
        new_list = []
        first_note = k
        new_list.append(first_note)
        
        new_note = first_note
        new_note = raise_note(new_note, 1)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 1)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 0.5)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 1)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 1)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 1)
        new_list.append(new_note)
        
        new_note = raise_note(new_note, 0.5)
        new_list.append(new_note)
        
        new_list = list(filter(lambda x: '#' in x, new_list))
        
        final_dict = {diez[:-1]:diez for diez in new_list}
        
        return final_dict
    else:
        return []


## Time to Convert!

my_notes = ['sol','do','do','mi','sol','sol','sol', 'si']
key = ['si', 'major']
expected = ['do', 'fa#', 'fa#', 'mi']

# final_converter(my_notes, key)



    
# Streamlit part
#############################################33
st.title('Converter')


input_col1, input_col2 = st.columns(2)
txt = input_col1.text_input('Your note here:', 'do re mi fa')
key = input_col2.text_input('Your key here:', 're major')

def update_text(n):
    global txt
    txt = txt + n
    st.markdown(txt)
    
def show_note(*n):
    update_text(n[0])

# cols = st.columns(len(all_notes))
# btns_dict = {f'btn {note}': cols[i].button(note, on_click=show_note, args=(note, txt)) for (i, note) in enumerate(all_notes)}


# notes_txt = st.text_input('Your original notes', txt)


st.write(txt)
my_notes = txt.strip().split()
key = key.strip().split()

if st.button('Convert!'):
    st.markdown('<h3 style="text-align:center"><u>Output</u></h3>', unsafe_allow_html=True)
    st.subheader(' '.join(final_converter(my_notes, key)))