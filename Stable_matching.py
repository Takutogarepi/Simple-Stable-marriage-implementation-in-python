import collections
Preffered_rankings_for_boys = {
    'John'  : ['Jane','Trish','Rose','Lucy','Lizzy','Lindi'],
    'James' : ['Jane','Lindi','Lizzy','Lucy','Trish','Rose'],
    'Bruce' : ['Rose','Lucy','Jane','Lizzy','Lindi','Trish'],
    'Tom'   : ['Lucy','Trish','Rose','Jane','Lindi','Lizzy'],
    'Tim'   : ['Trish','Lindi','Lizzy','Jane','Lucy','Rose'],
    'Frank' : ['Lizzy','Lucy','Lindi','Rose','Trish','Jane']
    }

Preffered_rankings_for_girls ={
    'Jane'  : ['Frank','Tim','Tom','John','Bruce','James'],
    'Rose'  : ['Bruce','James','Tim','Frank','Tom','John'],
    'Lindi' : ['John','Frank','Tom','Bruce','Tim','James'],
    'Lucy'  : ['Tom','James','Tim','Frank','John','Bruce'],
    'Lizzy' : ['Bruce','Tom','James','John','Tim','Frank'],
    'Trish' : ['Tom','Frank','James','John','Tim','Bruce']
}

#a list of the potential engagements
temporarily_engaged =[]

#boys yet to engage
free_boys = []

def init_free_boys():
    for boy in Preffered_rankings_for_boys:
        free_boys.append(boy)

def stable_match():
    while(len(free_boys)> 0):
        for boy in free_boys:
            start_matching(boy)



def start_matching(boy):
    print("we're dealing with %s"%(boy))
    for girl in Preffered_rankings_for_boys[boy]:
        matched = [couple for couple in temporarily_engaged if girl in couple ]
        if(len(matched)==0):
            temporarily_engaged.append([boy, girl])
            free_boys.remove(boy)
            print('%s is no longer free, he is temporarily engaged to %s'%(boy,girl))
            break
        elif(len(matched)>0):
            print('%s is already taken '%(girl))

            current_boy = Preffered_rankings_for_girls[girl].index(matched[0][0])
            potential_boy = Preffered_rankings_for_girls[girl].index(boy)

            if (current_boy < potential_boy):
                print('She is satisfied with %s'%(matched[0][0]))
            else:
                print('%s is better than %s'%(boy,matched[0][0]))
                print('Making %s free again and temporarily engaging %s and %s'%(matched[0][0],boy,girl))

                free_boys.remove(boy)

                free_boys.append(matched[0][0])

                matched[0][0] = boy
                break


def main():
    init_free_boys()
    stable_match()
    print(temporarily_engaged)

main()