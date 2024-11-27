import tkinter as tk
from tkinter import scrolledtext

web_superkey_map = "uph2!iqu7aish#6ahk@6Aed^ee6utha_u?rohgh1i-eHaey3ieY=0jiJah%z4ou2"
telnet_superkey_map = "Iex5ahb#oh3o@wai!hoh8q-uaeye+9ti@4Oob=ohm4uP!heiN?u3thei:g<aec"

def create_web_superkey(imei):
    v4 = imei
    v3 = []
    v7 = 1
    
    for i in range(10):
        for j in range(15):
            v7 += ord(v4[(j + i) % 15]) * ((i + 1) * (j + 1) & 0xFF)
    
        v7 = (283 * v7) & 0x3F
        v3.append(web_superkey_map[v7])
    return ''.join(v3)

def create_telnet_superkey(imei):
    v3 = []
    v6 = len(imei)
    
    if v6 != 12:
        return "LengthError"
    
    v9 = 1
    for i in range(10):
        for j in range(v6):
            char_code = ord(imei[(j + i) % v6])
            if v9 > 0xFFFFFF:
                v9 = ~v9 & 0xFFFFFF
            v9 += char_code * ((i + 1) * (j + 1) & 0xFF)
            if v9 > 0xFFFFFF:
                v9 = ~v9 & 0xFFFFFF
        v9 = (253 * v9) & 0x3F
        v3.append(telnet_superkey_map[v9])
    return ''.join(v3)

root = tk.Tk()
root.title("Super Key Generator")

input_label = tk.Label(root, text="Enter IMEI below:")
input_label.pack(pady=10)
input_text = tk.Entry(root, width=50)
input_text.pack(pady=10)

function_label = tk.Label(root, text="Select Function:")
function_label.pack(pady=10)
function_var = tk.StringVar(value="Generate Web Super Key")
function_options = {
    "Generate Web Super Key": "create_web_superkey",
    "Generate Telnet Super Key": "create_telnet_superkey"
}
function_menu = tk.OptionMenu(root, function_var, *function_options.keys())
function_menu.config(width=24)
function_menu.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=50, height=5, wrap=tk.WORD)
result_text.pack(pady=20)

def generate_key():
    imei = input_text.get()
    func_name = function_options[function_var.get()]
    
    if func_name == "create_web_superkey":
        if len(imei) != 15:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error: The input string for the Web Super Key must be 15 characters long.\n")
        else:
            result = create_web_superkey(imei)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, (
                f"Web Super Key: {result}\n"
                "The Web login username is usually 'superadmin',\n"
                "If your version is higher than 1.12.11.1, \n"
                "then your superuser is 'Gztz@83583#'\n"
                "JUST TRY BOTH!'\n"
            ))
    elif func_name == "create_telnet_superkey":
        if len(imei) != 12:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error: The input string for the Telnet Super Key must be 12 characters long.\n")
        else:
            result = create_telnet_superkey(imei)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Telnet Super Key: {result}\n")

generate_button = tk.Button(root, text="Generate Super Key", command=generate_key)
generate_button.pack(pady=20)

root.mainloop()