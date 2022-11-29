import assistant_details
from output_module import output
from time_module import get_time, get_date
from database import *
from output_module import output
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
from voice_input import cmd


def process(query):
    answer = get_answer_from_memory(query)

    if answer == "get time":
        return "time is:" + get_time()
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "tell date":
        return "date is:" + get_date()
    elif answer == "on speak":
        return turn_speech_on()
    elif answer == "off speak":
        return turn_speech_off()

    elif answer == "change name":
        output("Okey! what do you want to call me")
        temp = take_input()
        if temp == assistant_details.name:
            return "cant't change . I think you're happy with my old name"
        else:
            update_name(temp)
            assistant_details.name = temp
            return "now you can call me " + temp


    else:
        output("dont know this one should i search on internet ?")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        output("can you please tell me what is mean")
        ans = take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans = ans.strip()
            value = get_answer_from_memory(ans)
            if value == "":
                return "cant help this one"
            else:
                insert_question_and_answer(query, value)
                return "thanks i will remember for the next time"
        else:
            return "can't help with this one"
