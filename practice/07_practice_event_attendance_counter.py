'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. Create an EventAttendee class with a class variable total_attendees
   initialized to 0.
2. In __init__, store the attendee name and increment total_attendees.
3. After creating five attendees, print the class variable to show the
   total number registered.
'''

class EventAttendance:
    total_attendees = 0
    def __init__(self, attendee):
       self.attendee = attendee
       EventAttendance.total_attendees += 1

attendee1 = EventAttendance("John")
attendee2 = EventAttendance("Bill")
attendee3 = EventAttendance("Jill")
attendee4 = EventAttendance("Quincy")
attendee5 = EventAttendance("Adams")

print(EventAttendance.total_attendees)
