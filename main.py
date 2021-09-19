# Loop Back to this point once code generated
loop = 1
while(loop < 10):
    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    # Display the story based on the user input
    print("------------------------------------------")
    print(f"Be kind to your {noun} - footed {p_noun}")
    print(f"For a duck maybe someday's {noun2},",",")
    print(f"Be kind to your {p_noun}, in {place}")
    print(f"Where the weather is always {adjective}.\n")
    print(f"You may think that is this the {noun3},")
    print(f"Well it is.")
    print("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
