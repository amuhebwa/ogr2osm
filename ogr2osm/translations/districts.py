"""
Translations for districts(level 2)
created by Aggrey Muhebwa | Mountbatten Ltd(U)

"""
def acceptableNames(name):
         #Create an empty dictionary and populate it with possible suffix
        lookup = {} 
        lookup.update({"region,C,50":"region"})
        lookup.update({"id,N,6,1":"id"})
        lookup.update({"district,C,20":"district"})

def filterTags(attrs):
        if not attrs :
            return
        tags = {}
        if(ttrs["region,C,50"]):
            tags.update({'region':acceptableNames(attrs['region,C,50'])})
        if(attrs['id,N,6,1']):
            tags.update({'id':acceptableNames(attrs['id,N,6,1'])})
        if(attrs["district,C,20"]):
            tags.update({'district':acceptableNames[attrs['district,C,20']]})
        return tags
