# -*- coding: utf-8 -*-
import sys
from data import *
from workflow import Workflow3, ICON_NOTE
from math_util import write_roman, write_aegean, write_chinese

def main(wf):

    query = wf.args[0].strip()

    # numbers
    if len(query)>0 and query[0] >= '0' and query[0]<='9':
        lookup_set = dict_number

        # Fractions
        if query in dict_number_fraction:
            result = dict_number_fraction[query]
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Vulgar Fraction")


        # Pure Digits
        i = 0
        num = 0
        while i < len(query) and query[i] <= '9' and query[i]>= '0':
            num = num * 10
            num = num + ord(query[i]) - ord('0')
            i = i + 1
        
        if i < len(query):
            num = -1
            
        # Roman Letters
        if num < 5000 and num > 0:
            result = str(write_roman(num))
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Roman: " + str(num)) 
            
        # Aegean Letters
        if num < 100000 and num > 0:
            result = str(write_aegean(num))
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Aegean: " + str(num)) 

        # Chinese Letters
        if num >= 0:
            result = str(write_chinese(num))
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Chinese: " + str(num)) 

        # Circled Number
        if num >= 0 and num<=50:
            result = dict_number_long['Circled'][num]
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Circled") 

        # Full Stop
        if num >= 1 and num<=20:
            result = dict_number_long['Full Stop'][num]
            wf.add_item(title=result, arg=result, valid=True,
                subtitle="Full Stop") 

        # subset
        for style, lookup in lookup_set.items():

            convert = []
            to_search = query 

            for c in query:
                if c>='0' and c<='9':
                    index = ord(c) - ord('0')
                    z = lookup[index]
                    convert.append(z)
                else:
                    convert.append(c.encode("utf-8"))
            
            result = ''.join(convert)
            wf.add_item(title=result, arg=result, valid=True,
                subtitle=style)




    # alphabets
    else:
        lookup_set = dict_letter
        if query.startswith("fun "):
            lookup_set = dict_glitch 
            query = query[4:]

        for style, lookup in lookup_set.items():

            convert = []
            to_search = query 

            for c in query:
                if c>='a' and c<='z':
                    index = ord(c) - ord('a')
                    z = lookup[index]
                    convert.append(z)
                elif c>='A' and c<='Z':
                    index = ord(c) - ord('A') + 26
                    z = lookup[index]
                    convert.append(z)
                else:
                    convert.append(c.encode("utf-8"))

                result = ''.join(convert)

            wf.add_item(title=result, arg=result, valid=True, subtitle=style)

        ## Inverted
        invert_map = {
            ',':"'",'.':'˙','?':'¿','!':'¡','"':'„',
            '[':']',']':'[','(':')',')':'(','{':'}','}':'{','<':'>','>':'<',
            '_':'¯','^':' ̮','&':'⅋',
            '1':'⇂','2':'Ƨ','3':'Ɛ','4':'h','5':'S','6':'9','7':'L','9':'6'
        }
        convert = []
        lookup = dict_glitch['Inverted']
        for c in query:
            if c>='a' and c<='z':
                index = ord(c) - ord('a')
                z = lookup[index]
                convert.append(z)
            elif c>='A' and c<='Z':
                index = ord(c) - ord('A') + 26
                z = lookup[index]
                convert.append(z)
            elif c in invert_map:
                convert.append(invert_map[c])                     
            else:
                convert.append(c.encode("utf-8"))

        result = ''.join(reversed(convert))
        wf.add_item(title=result, arg=result, valid=True, 
            subtitle="Inverted")


    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow3()
    sys.exit(wf.run(main))

