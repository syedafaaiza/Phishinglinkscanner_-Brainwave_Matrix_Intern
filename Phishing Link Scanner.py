#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import re
import tldextract
import tkinter as tk
from tkinter import messagebox

# Function to fetch data from URL
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Unable to connect to {url}")
    except requests.exceptions.Timeout:
        print(f"Error: Timeout while trying to access {url}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

# Function to extract domain from URL
def extract_domain(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    return domain

# Function to check for phishing patterns in page content
def check_for_phishing_patterns(page_content):
    patterns = [
        r"login",  # phishing sites often request login
        r"account",  
        r"update",
        r"verify",
        r"password",
        r"secure"
    ]
    for pattern in patterns:
        if check_pattern(pattern, page_content):
            return True
    return False

# Function to check if a pattern is found
def check_pattern(pattern, page_content):
    if re.search(pattern, page_content, re.IGNORECASE):
        return True
    return False

# Function to scan the URL
def scan_url(url):
    page_content = fetch_data(url)
    if page_content:
        domain = extract_domain(url)
        result = f"Scanning Domain: {domain}\n"
        
        # Check for phishing patterns in the page content
        if check_for_phishing_patterns(page_content):
            result += f"Warning: Possible phishing attempt detected in {url}"
        else:
            result += f"Safe: No phishing indicators found in {url}"
        
        return result
    else:
        return f"Failed to fetch content from {url}"

# Function to check URL length
def check_url_length(url):
    if not url:  # Ensure the URL is not empty
        return "Invalid URL: No URL provided"
    if len(url) < 15:
        return f"Suspicious URL: {url} (URL too short)"
    else:
        return f"URL length is fine: {url}"

# GUI Functionality
def scan_button_action():
    url = url_entry.get()  # Get URL from input field
    if url:
        result_text.delete(1.0, tk.END)  # Clear the previous results
        # Check URL length
        length_check_result = check_url_length(url)
        result_text.insert(tk.END, length_check_result + "\n")
        
        # Scan the URL for phishing indicators
        scan_result = scan_url(url)
        result_text.insert(tk.END, scan_result + "\n\n")  # Display the scan result in the Text widget
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL")

# Setup the GUI
root = tk.Tk()
root.title("Phishing URL Scanner")
root.geometry("500x400")  # Set window size

# Set background color for the window
root.configure(bg="#2C3E50")  # Dark background for better contrast

# Header Frame
header_frame = tk.Frame(root, bg="#34495E")
header_frame.pack(fill="x", pady=10)

header_label = tk.Label(header_frame, text="Phishing URL Scanner", font=("Helvetica", 16, "bold"), fg="white", bg="#34495E")
header_label.pack()

# URL Input Frame
input_frame = tk.Frame(root, bg="#2C3E50")
input_frame.pack(pady=10)

url_label = tk.Label(input_frame, text="Enter URL:", font=("Arial", 12), fg="white", bg="#2C3E50")
url_label.grid(row=0, column=0, padx=5)
url_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
url_entry.grid(row=0, column=1, padx=5)

# Scan Button
scan_button = tk.Button(root, text="Scan URL", font=("Arial", 12, "bold"), bg="#E74C3C", fg="white", command=scan_button_action)
scan_button.pack(pady=10)

# Results Frame
result_frame = tk.Frame(root, bg="#2C3E50")
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Scan Results:", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50")
result_label.pack(anchor="w", padx=10)

result_text = tk.Text(result_frame, height=10, width=55, font=("Arial", 10), wrap="word", borderwidth=2, relief="sunken")
result_text.pack(padx=10, pady=5)

# Run the GUI loop
root.mainloop()


# In[ ]:




