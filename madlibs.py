"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

# Add templates in list or dictionary form, 
madlibs_list = [f"Most doctors agree that bicycle of **verb  is a/an **adjective form of exercise. **verb  a bicycle enables you to develop your **part_of_body muscles as well as **adverb  increase the rate of a **part_of_body beat. More **noun around the world **verb bicycles than drive **animals. No matter what kind of **noun you **verb, always be sure to wear a/an **adjective helmet. Make sure to have  **color  reflectors too!", "There once was a **color **noun sitting in the Hackbright Lab. When **person went to pick it up, it burst into flames in a totally **adjective way."]

# randomly select a template when user says they want to play a game


# pull out fields that need user input from the template


# game.html needs to ask for inputs that correspond with the template


# show_madlib() also needs to request / process inputs that correspond with the template

@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():

    answer = request.args.get("game")
    if answer == "no":
        return render_template("goodbye.html")
    elif answer == "yes":
        # randomly pick madlib from list
        chosen_madlib = choice(madlibs_list)
        # create input_text_fields
        words = chosen_madlib.split(' ')
        # input_text_fields = ""
        # for word in words:
        #     [f'<label> {prompt}: <input type="text" name={prompt}> </label>' for prompt in words for '**' in prompt]

        # choses_madlib = choice(list(madlibs_dict.values))
        # words + chosen_madlib.split('')
        # input_text_fields = "".join([f'<label> {prompt[2:]}: <input type = "text" name = "{prompt}"></label>' for prompt in words if prompt.startswith('**')])
        # return render_template("game.html", input_text_fields=input_text_fields)

        # dict = {key (#): 'prompt'}
        # set counter to 0
        counter = 0
        # create blank dictionary
        prompt_dict = {}
        for word in words:
            if word.startswith('**'):
                # prompt_dict[counter = {'prompt: word, 'input':''}]
                prompt_dict[counter] = word[2:] 
                counter += 1
        # iterate over word in words (for loop)

            # if words starts with **

                # add counter:word pair to dictionary

                # increment counter by one

        return render_template("game.html", prompt_dict=prompt_dict)
    else:
        return render_template("error.html")
    
@app.route("/madlib")
def show_madlib():

    # randomly pick madlib from list

    # create selected_madlib
    
    # Code from first section of lab, kept for reference
    # noun = request.args.get("noun")
    # adjective = request.args.get("adjective")
    # person = request.args.get("person")
    # color = request.args.get("color")


    # madlib_dict = {
    #     'color': color,
    #     'person': person,
    #     'adjective': adjective,
    #     'noun': noun,
    # }
    
    return render_template("madlib.html", selected_madlib)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
