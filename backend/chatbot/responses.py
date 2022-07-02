from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey friend. How are you? How can I help you?")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")


class PassingGrade(GenericRandomResponse):
    choices = ("College requirement is D or 55 marks or more. Department requirement is 60 marks or more. Major requirement is C or 67 marks",
               "College requirement is D or 55 marks or more. Department requirement is 60 marks or more. Major requirement is C or 67 marks")


class Ielts(GenericRandomResponse):
    choices = ("Bachelor: IELTS 5.0 or higher. Advanced diploma: IELTS 4.5 or higher",
               "Bachelor: IELTS 5.0 or higher. Advanced diploma: IELTS 4.5 or higher")


class EnglishTest(GenericRandomResponse):
    choices = ("Bachelor: 71-100,Advanced diploma: 64-70, Diploma: 50-63",
               "Bachelor: 71-100,Advanced diploma: 64-70, Diploma: 50-63")
