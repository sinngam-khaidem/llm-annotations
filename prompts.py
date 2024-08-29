def prompt1(context, utterance):
    message = """
    TASK:
    You will be given a context and an utterance, and your task is to determine how sarcastic the given utterance is using the context.
    Rate each utterance on a scale of 0 to 10 for sarcasm, with 0 being completely non-sarcastic and 10 being extremely sarcastic.

    To give you and idea:
    Sarcasm is a subtle form of language in which people express the opposite of what is implied.
    Being humorous doesn't necessarily make the utterance sarcastic.
    
    Given the following few shot examples (delimited by <examples></examples>)
    <examples>
    Context: so mr thompson, you say you have some programming skills???
    Utterance: probably referring to the "readability" certification. it's not hard, it just exempts you from needing a peer review on commits and enables you to approve other people's commits. totally overblown. i had readability in go, python, golang, and c when i worked there. you use an existing commit to request a readability certification.
    Your Response: {"Rating": "0.5"}
    ----

    Context: we’ve come full circle
    Utterance: there are three things you don’t discuss with strangers: religion, politics, and star wars.
    Your Response: {"Rating": "9.5"}
    ----

    Context: "clone wars? what are you talking about?"
    Utterance: i am one of the guys that saw star wars as a little boy (age 7, saw it 1978) the line was perfect!it immediately triggered my imagination of a dystopia where humans were cloned for being soldiers and maybe rebelled or tried to dominate which lead to a war. not far away from what was created later.
    Your Response: {"Rating": "0.7"}
    ----

    Context: keepers of peace, but in the most violent way
    Utterance: cut their hand off. that's the sith way. or go full obi and cut both their arms and legs off. that'll show em. bastards.
    Your Response: {"Rating": "8.7"}
    ----

    Context: people dont like videos cut too short.
    Utterance: then later, they would cut off just one wire from a 1,000,000 volt power grid
    Your Response: {"Rating": "2.3"}
    ----

    Context: roommates rice cooker has turned into brain-like tissue. he refuses to clean it, and leaves it on the shared kitchen counter.
    Utterance: that’s a biohazard.
    Your Response: {"Rating": "8.3"}
    ----

    Context: found a camera in my air b&b. it was halfway behind the painting with only the lens peeking out. discovered it because we heard it clicking after me and my girl got out of the shower.
    Utterance: that's not mildly infuriating, that's much worse.
    Your Response: {"Rating": "0.6"}
    ----

    Context: sick fuck fuses dogs togeter with black sorcery
    Utterance: i'm so confused rn
    Your Response: {"Rating": "8.4"}
    ----

    Context: this restaurant covered up the "no tip" option with a sticker to force tipping
    Utterance: percentage = 0%
    Your Response: {"Rating": "2.4"}
    ----

    Context: looks like i won't be listening to my new vinyl record. thanks, usps
    Utterance: how can an assigned delivery person not know the basic rule of don't bend the damn packages?!
    Your Response: {"Rating": "1.5"}
    </examples>
    ----
    Context: someone put a paper trump sticker on my sister’s car because we have a biden sign in our front yard.
    Utterance: that’s so stupid. i don’t care if you’re a trump supporter or a biden supporter, do not vandalize other peoples property because they like a different candidate then you.
    Your Response: {"Rating": "0.6"}
    """

    message = message + f"""
    Generate a valid JSON for the following(delimited by <test></test>)
    <test>
    Context: {context}
    Utterance: {utterance}
    Your Response: 
    </test>
    Respond only with valid JSON. Do not write an introduction or summary.
    """
    
    return message

def prompt2(context, utterance):
    message = """
    TASK:
    You are give a context and an utterance. Analyse the sarcasm of the utterance, and respond with one of the following labels: 0(Non-Sarcastic) or 1(Sarcastic)
    Make sure the utterance implies a strong, unambiguous sarcastic impression, using the context provided.
    
    Given the following few shot examples (delimited by <examples></examples>)
    <examples>
    Context: so mr thompson, you say you have some programming skills???
    Utterance: probably referring to the "readability" certification. it's not hard, it just exempts you from needing a peer review on commits and enables you to approve other people's commits. totally overblown. i had readability in go, python, golang, and c when i worked there. you use an existing commit to request a readability certification.
    Your Response: {"Rating": "0"}
    ----

    Context: we’ve come full circle
    Utterance: there are three things you don’t discuss with strangers: religion, politics, and star wars.
    Your Response: {"Rating": "1"}
    ----

    Context: "clone wars? what are you talking about?"
    Utterance: i am one of the guys that saw star wars as a little boy (age 7, saw it 1978) the line was perfect!it immediately triggered my imagination of a dystopia where humans were cloned for being soldiers and maybe rebelled or tried to dominate which lead to a war. not far away from what was created later.
    Your Response: {"Rating": "0"}
    ----

    Context: keepers of peace, but in the most violent way
    Utterance: cut their hand off. that's the sith way. or go full obi and cut both their arms and legs off. that'll show em. bastards.
    Your Response: {"Rating": "1"}
    ----

    Context: people dont like videos cut too short.
    Utterance: then later, they would cut off just one wire from a 1,000,000 volt power grid
    Your Response: {"Rating": "0"}
    ----

    Context: roommates rice cooker has turned into brain-like tissue. he refuses to clean it, and leaves it on the shared kitchen counter.
    Utterance: that’s a biohazard.
    Your Response: {"Rating": "1"}
    ----

    Context: found a camera in my air b&b. it was halfway behind the painting with only the lens peeking out. discovered it because we heard it clicking after me and my girl got out of the shower.
    Utterance: that's not mildly infuriating, that's much worse.
    Your Response: {"Rating": "0"}
    ----

    Context: sick fuck fuses dogs togeter with black sorcery
    Utterance: i'm so confused rn
    Your Response: {"Rating": "1"}
    ----

    Context: this restaurant covered up the "no tip" option with a sticker to force tipping
    Utterance: percentage = 0%
    Your Response: {"Rating": "0"}
    ----

    Context: looks like i won't be listening to my new vinyl record. thanks, usps
    Utterance: how can an assigned delivery person not know the basic rule of don't bend the damn packages?!
    Your Response: {"Rating": "0"}
    </examples>
    ----
    Context: someone put a paper trump sticker on my sister’s car because we have a biden sign in our front yard.
    Utterance: that’s so stupid. i don’t care if you’re a trump supporter or a biden supporter, do not vandalize other peoples property because they like a different candidate then you.
    Your Response: {"Rating": "0"}
    """

    message = message + f"""
    Generate a valid JSON for the following(delimited by <test></test>)
    <test>
    Context: {context}
    Utterance: {utterance}
    Your Response: 
    </test>
    Respond only with valid JSON. Do not write an introduction or summary.
    """
    
    return message

prompt3 = """
TASK:
You will be given a context and an utterance, and your task is to determine how sarcastic the given utterance is.
Rate each utterance on a scale of 0 to 10 for sarcasm, with 0 being completely non sarcastic and 10 being extremely sarcastic.

To give you and idea:
Sarcasm is a subtle form of language in which people express the opposite of what is implied.
Th utterance must imply a strong sarcastic irony, insult, or juxtaposition when considered together with the context.
If the utterance fails to do so , the utterance is non sarcastic by default.
Most utterances does not imply any sarcasm at all.

Given the following few shot examples (delimited by <examples></examples>)
<examples>
Context: so mr thompson, you say you have some programming skills???
Utterance: probably referring to the "readability" certification. it's not hard, it just exempts you from needing a peer review on commits and enables you to approve other people's commits. totally overblown. i had readability in go, python, golang, and c when i worked there. you use an existing commit to request a readability certification.
Your Response: {"Rating": "0.5"}
----

Context: we’ve come full circle
Utterance: there are three things you don’t discuss with strangers: religion, politics, and star wars.
Your Response: {"Rating": "9.5"}
----

Context: "clone wars? what are you talking about?"
Utterance: i am one of the guys that saw star wars as a little boy (age 7, saw it 1978) the line was perfect!it immediately triggered my imagination of a dystopia where humans were cloned for being soldiers and maybe rebelled or tried to dominate which lead to a war. not far away from what was created later.
Your Response: {"Rating": "0.7"}
----

Context: keepers of peace, but in the most violent way
Utterance: cut their hand off. that's the sith way. or go full obi and cut both their arms and legs off. that'll show em. bastards.
Your Response: {"Rating": "8.7"}
----

Context: people dont like videos cut too short.
Utterance: then later, they would cut off just one wire from a 1,000,000 volt power grid
Your Response: {"Rating": "2.3"}
----

Context: roommates rice cooker has turned into brain-like tissue. he refuses to clean it, and leaves it on the shared kitchen counter.
Utterance: that’s a biohazard.
Your Response: {"Rating": "8.3"}
----

Context: found a camera in my air b&b. it was halfway behind the painting with only the lens peeking out. discovered it because we heard it clicking after me and my girl got out of the shower.
Utterance: that's not mildly infuriating, that's much worse.
Your Response: {"Rating": "0.6"}
----

Context: sick fuck fuses dogs togeter with black sorcery
Utterance: i'm so confused rn
Your Response: {"Rating": "8.4"}
----

Context: this restaurant covered up the "no tip" option with a sticker to force tipping
Utterance: percentage = 0%
Your Response: {"Rating": "2.4"}
----

Context: looks like i won't be listening to my new vinyl record. thanks, usps
Utterance: how can an assigned delivery person not know the basic rule of don't bend the damn packages?!
Your Response: {"Rating": "1.5"}
</examples>
----
Context: someone put a paper trump sticker on my sister’s car because we have a biden sign in our front yard.
Utterance: that’s so stupid. i don’t care if you’re a trump supporter or a biden supporter, do not vandalize other peoples property because they like a different candidate then you.
Your Response: {"Rating": "0.6"}
"""


image_prompt = f"""
TASK:
You will be given an image, and your task is to determine whether the image contains sarcasm. 
Indicate your response with a 1 if sarcasm is detected and a 0 if it is not sarcastic.

EXAMPLES:
"""