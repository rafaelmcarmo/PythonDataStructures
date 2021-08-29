text = "X-DSPAM-Confidence:    0.8475";
result = text.find('0.8475')
_result=float(text[23:29])
print(_result)
