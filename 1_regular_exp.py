import re

# Sample text
text = """
Hello, my name is John Doe. You can contact me at john.doe@example.com .
My website is https://www.johndoe.com and my phone number is 123 456 7890.
I live in New York, NY 10001 2004-09-10.
"""
email= r'[A-Za-z0-9.]+@[A-Za-z].[a-zA-z.]{2,}'
url =r'https?://[\w.]+\.[a-zA-Z]{2,}'
date=r'\d{4}-\d{2}-\d{2}'
name =r'\b[A-Z][a-z]* [A-Z][a-z]*\b'
ph =r'\d{3} \d{3} \d{4}'
zip= r'\d{5}'
print(re.findall(email,text))
print(re.findall(url,text))
print(re.findall(date,text))
print(re.findall(name,text))
print(re.findall(ph,text))
print(re.findall(zip,text))
