CW = ["Did you submitted Cw Submission on Time?"]
for x in CW:

    print(x)

answer = input("Yes or No: ")
if answer.lower() == "yes":
    print("Full mark")
    exit(0)

else:
    print("Within 24 hours ?")
    answer = input("Yes or No: ")
    if answer.lower() == "yes":
        print("Is there a valid reason for Late Submission ? ")

        answer = input("Yes or No: ")
        if answer.lower() == "yes":
            print("MC\nAccepted? ")
            answer = input("Yes or No: ")
            if answer.lower() == "yes":
                print('Full Mark')
            else:
                print("-10 marks from overall mark but not below 40")
        else:
            print("-10 marks from overall mark but not below 40")
    else:
        print("Submitted within 5 days?")
        answer = input("Yes or No: ")

        if answer.lower() == "yes":
            print(" Is there a valid reason ? ")
            answer = input("Yes or No: ")
            if answer.lower() == "yes":
                print('MC (late submission option)\n Accepted ? ')
                answer = input("Yes or No: ")
                if answer.lower() == "yes":
                    print("Full mark")
                else:
                    print("Mark = 0")
            else:
                print("Mark=0")
        else:
            print("Is there a valid reason ? ")
            answer = input("Yes or No: ")
            if answer.lower() == "yes":
                print("MC(non-deferral) before specified deadline\nAccepted\nDeferral reassessment")
            else:
                print("Mark = 0")
