def split_bill(tot_money,people):
    if isinstance(tot_money,int) and isinstance(people,int) and people>0 :
        share=tot_money//people
        print("Each person's share =",share)
    else:
        print("invalid input")
tot_money=1250
people=4
split_bill(tot_money,people)            