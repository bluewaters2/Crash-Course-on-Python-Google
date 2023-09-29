def combine_lists(list1, list2):


  combined_list = "" # Initialize an empty list variable
  for i in range(len(list1)-1,-1,-1): # Reverse the order of "list1"
    list2.append(list1[i]) # Combine the two lists 
  
  return list2
  
Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


print(combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
