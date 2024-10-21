# Phishinglinkscanner_-Brainwave_Matrix_Intern
Phishing URL Scanner This Python project provides a simple and intuitive tool to check URLs for phishing indicators by analyzing the page content and URL structure. It features a user-friendly graphical interface (built with Tkinter) that allows users to input URLs and receive real-time feedback on potential phishing risks.

Key Features:
Domain Extraction: Extracts and displays the main domain from the provided URL using the tldextract library.
Phishing Pattern Detection: Scans the webpage content for common phishing-related keywords, such as "login", "password", "verify", and others.
URL Length Check: Identifies suspiciously short URLs, which are often used in phishing attacks.
Graphical User Interface (GUI): A clean and interactive GUI built with Tkinter for easy URL input and result visualization.
Real-Time Feedback: Provides immediate results on whether the URL is likely safe or could be a phishing attempt.

How It Works:
The user inputs a URL into the GUI.
The URL is scanned in two ways:
URL length check: Short URLs are flagged as potentially suspicious.
Content analysis: The webpage is fetched and searched for phishing keywords.
The results are displayed in the GUI, informing the user if phishing indicators were detected or if the URL is likely safe.

Technologies Used:
Python Requests: For fetching webpage content.
Tldextract: To extract and format domain names from URLs.
Regular Expressions (re): To search for phishing patterns in webpage content.
Tkinter: To build the GUI.

Example Usage:
1.Enter a URL like http://example.com in the URL input field.
2.Click "Scan URL."
3.View the results: either a warning about phishing indicators or a confirmation that the URL appears safe.
