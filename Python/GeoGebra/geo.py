import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math



# %matplotlib inline

def calc_func(l_rng=-5, h_rng=5, y_rng=100, func=None):
#     func_dict = {}
    x_vals = []
    y_vals = []
    is_defined = []
    divider = 100
    for x in range(l_rng*divider, (divider*h_rng)+1):    
        x = x/divider
        
        try:
            # ------------------------------------
            # Insert Expression Here:
            func_x = func(x)
            # ------------------------------------
            
            x_vals.append(x)
            y_vals.append(func_x)
            if abs(func_x) > int(y_rng):
                is_defined.append(999)
            elif func_exp == 0: 
                is_defined.append(-1)
            else:
                is_defined.append(1)
            
        except:
            x_vals.append(x)
            y_vals.append(0)
            is_defined.append(0)
    return pd.DataFrame({'X':x_vals, 'Y':y_vals, 'isDefined':is_defined})



def show_function(df):

    fig, ax = plt.subplots()
    
    df['isSwitch'] = df.apply(lambda x:  1 if ((x['Y'] != 0) and (x.name > 0) and (df.loc[x.name - 1, 'Y'] / df.loc[x.name, 'Y'] < 0)) or x['Y'] == 0 else 0  , axis=1)

    df_def = df[df['isDefined'] == 1]
    ax.plot(df_def['X'], df_def['Y'], marker='o', lw=0)

    df_Zero = df[df['isSwitch'] == 1]
    ax.plot(df_Zero['X'], df_Zero['Y'], marker='o', color='y', lw=0, markersize=12)

    df_undef = df[df['isDefined'] == 0]
    ax.plot(df_undef['X'], df_undef['Y'], marker='o', color='r', lw=0)

    axes_limit = 2

    if max(df_def['X'])+axes_limit >= 0 and min(df_def['X'])-axes_limit <= 0:
        ax.axvline(linewidth=1, color='k')
    if max(df_def['Y'])+axes_limit >= 0 and min(df_def['Y'])-axes_limit <= 0:    
        ax.axhline(linewidth=1, color='k')
#     plt.show()
    
    return fig




col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
params = col1.text_input("A", 0), col2.text_input("B", 1), col3.text_input("C", 0), col4.text_input("D", -10)
A, B, C, D = map(float, params)

def func_exp(x):
    return A*x**3 + B*x**2 + C*x + D


x = st.slider('x', max_value=1000, value=10)  # 👈 this is a widget
y = st.slider('y', max_value=1000, value=10)  # 👈 this is a widget
edges = x
highest_y = y

df = calc_func(-edges, edges, highest_y, func_exp)

mpl = show_function(df)

st.pyplot(mpl)
st.write(x, 'squared is', x * x)