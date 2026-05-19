from access_logic import *

#################################################
# CIS 540 Fundamentals of Information Security
# Homework #2 - Access Control
# Name: Todd S.
##################################################

class Main:
    # Declare and Initialize the Subjects (i.e. People):
    Alice = Subject("Top Secret", {"Graduate Student", "Staff"}, "Monday", 930)
    Bob = Subject("Confidential", {"Regular Faculty", "Staff"}, "Friday", 1445)
    Charlie = Subject("Secret", {"Adjunct Faculty"}, "Sunday", 1100)
    Dan = Subject("Confidential", {"Undergrad Student"}, "Saturday", 1200)
    Eva = Subject("Confidential", {"Graduate Student", "Staff"}, "Saturday", 2100)
    Frank = Subject("Confidential", {"Regular Faculty"}, "Sunday", 1600)

    # Show Alice's Access
    print("Alice: ")
    print(Alice.can_read(Object("Top Secret", {"Graduate Student", "Staff"})))
    print(Alice.can_write(Object("Top Secret", {"Graduate Student", "Staff"})))

    # Show Bob's Access
    print("\nBob: ")
    print(Bob.can_read(Object("Confidential", {"Regular Faculty"})))
    print(Bob.can_write(Object("Confidential", {"Regular Faculty"})))
        # Bob.can_write() is False due to the "No Write Down" principle because {Regular Faculty, Staff} is
        # not a subset of {Regular Faculty}.

    #Show Charlie's Access
    print("\nCharlie: ")
    print(Charlie.can_read(Object("Secret", {"Adjunct Faculty"})))
    print(Charlie.can_write(Object("Secret", {"Adjunct Faculty"})))
        # Charlie.can_read() is false because faculty cannot read on the weekend (Sunday).
        # Charlie.can_write() is false because adjunct faculty cannot write on the weekend.

    # Show Dan's Access
    print("\nDan: ")
    print(Dan.can_read(Object("Confidential", {"Undergrad Student"})))
    print(Dan.can_write(Object("Confidential", {"Undergrad Student"})))
        # Dan.can_write() is false because students can only write on weekeday's (not weekends).

    # Show Eva's Access
    print("\nEva: ")
    print(Eva.can_read(Object("Unclassified", {"Graduate Student", "Staff"})))
    print(Eva.can_write(Object("Unclassified", {"Graduate Student", "Staff"})))
        # Eva.can_read() is false because staff can only read during the weekdays (not weekend).
        # Eva.can_write() is false due to the "No Write Down" principle. Eva's clearance is Confidential but
        # the document's classification level is Unclassified, which would create a "no write down" conflict.

    # Show Frank's Access
    print("\nFrank: ")
    print(Frank.can_read(Object("Confidential", {"Regular Faculty"})))
    print(Frank.can_write(Object("Confidential", {"Regular Faculty"})))
        # Frank.can_read() is false because faculty can only read Monday-Friday, but Frank is trying to
        # read on Sunday.