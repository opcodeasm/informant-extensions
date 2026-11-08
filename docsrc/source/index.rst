####################################
Inform 7 Extension Guide
####################################

About This Guide
================

This guide is a standalone reference to the extensions distributed in the Inform
10.1 extension archive. Its purpose is to help Inform authors discover available
extensions, understand what they are intended to do, and find a starting point
for using them in source code. The extensions are grouped by their primary
purpose so that the guide can be browsed by capability as well as by extension
name. This first edition covers the 155 extensions in the archive that contain
an embedded ``DOCUMENTATION`` section. Extensions without embedded documentation
are intentionally omitted from this edition rather than described by inference
from their source code alone. Descriptions, authorship, version information, and
usage material in this guide are derived from the metadata and documentation
contained in the extensions themselves.

Using the Examples
==================

Where an extension supplies formal examples, this guide uses the shortest
complete author-provided example as the starting point, favoring a compact
introduction over a larger demonstration when the extension documentation
provides that choice. Inform documentation example markers are removed because
they are not part of the story source. Where no formal example is supplied but
the embedded documentation contains a short usage fragment, that material is
identified as **Documented usage** rather than presented as a complete working
story. The examples in this edition are derived from the extension documentation
but have not been independently compiled or tested as part of the preparation of
this guide.

Extension Categories
====================

The extensions are organized into functional categories according to their
primary purpose. Some extensions naturally overlap more than one area, so the
categories should be treated as a browsing aid rather than as a strict
classification of the Inform extension ecosystem. Within each category,
individual entries identify the extension and its author, summarize its stated
purpose, and provide documented usage material when available.

####################################
Conversation, Characters & NPCs
####################################

Assumed Conversers
==================

**Author:** Michael Martin | **Version:** 3.2

A minimal extension that makes the NPC optional in ASK NPC ABOUT TOPIC and TELL
NPC ABOUT TOPIC commands.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Conversation Nodes
==================

**Author:** Eric Eve | **Version:** 7

Builds on Conversational Defaults and adds the ability to define particular
points in a conversational thread (nodes) at which particular conversational
options become available.

**Basic example:** Sarah's Jealous Suspicions

Putting convnodes through their paces.

.. code-block:: inform7

   Part 1 - Setup and Map

   Include Conversation Nodes by Eric Eve.

   The Hall is a room. "Doors lead off in all directions from here, but the only important one is to the north, leading to the Lounge where Sarah is waiting for you."

   The Lounge is north of the Hall. "Although you've spent many cosy hours in here with Sarah, today the atmosphere feels decidedly chilly."

   Sarah is a woman in the lounge. "Sarah is standing in the middle of the Lounge, looking none too pleased with you."
   The description is "You wish she didn't look quite so suspicious of you."

   Part 2 - Sarah-Jealous-Node

   sarah-jealous-node is a closed convnode.

   After going to the Lounge for the first time:
     initiate a conversation with Sarah at sarah-jealous-node;
     continue the action.

   node-termination for sarah-jealous-node when going:
   now conversed-this-turn is true;
   say "'Don't you walk away while I'm talking to you!' Sarah storms, 'I asked you a question: are you seeing another woman?'"

   node-termination for sarah-jealous-node when saying goodbye to Sarah:
   now conversed-this-turn is true;
   say "'Don't you 'goodbye' me!' Sarah snaps, 'Answer my question: are you seeing another woman?'"

   response for sarah-jealous-node when saying yes:
   say "[node sarah-therapist-node]'Yes, I am, but only for psychotherapy sessions, and the therapist is old enough to be my grandmother!' you reply.[paragraph break]'Who is this woman?' she demands, 'What's her name?'"

   response for sarah-jealous-node when saying no:
   say "[leavenode]'No, of course not, you know you're the only woman in my life!' you protest.[paragraph break]'Very well,' she sighs, slightly mollified, 'Only Mary said - well, never mind, what Mary said.'"

   default response for sarah-jealous-node:
   say "'Don't try to change the subject!' she storms, 'I asked if you were seeing another woman. Well, are you? Yes or no!'"

   node-introduction for sarah-jealous-node:
   say "'Are you seeing another woman?' Sarah demands, wasting no time on pleasantries.[paragraph break](You could say yes or no)[paragraph break]"

   node-continuation for sarah-jealous-node:
   if a random chance of 1 in 2 succeeds,
   say "'Hey! Didn't you hear me?' Sarah demands, 'I asked you if you were seeing another woman - well, are you?'"

   Part 3 - Sarah-Therapist-Node

   sarah-therapist-node is an closed convnode.

   node-introduction for sarah-therapist-node:

Conversation Package
====================

**Author:** Eric Eve | **Version:** 3

This extension includes both Conversation Nodes and Conversation Suggestions,
and makes the suggestions aware of conversation nodes. It therefore includes the
complete conversational system in one package. It also requires Conversation
Responses, Conversational Defaults, Conversation Framework and Epistemology. The
documentation for this extension give some guidance on how these other
extensions can be mixed and matched.

**Basic example:** Consultation

A nodal conversation complete with suggestions, not that they help too much with
this doctor!

.. code-block:: inform7

   Part 1 - Setup

   Include Conversation Package by Eric Eve.

   To say /p: say paragraph break.
   To say /l: say line break.

   your symptoms are a familiar thing.
   the weather is a familiar thing.
   advice-suggestion is a misc-suggestion. 
   The printed name is "ask him for advice".

   Part 2 - Scenario

   The Doctor's Surgery is a room.

   Doctor Kilpatient is a man in the Surgery. "Doctor Kilpatient is sitting behind his desk, looking at you with the air of a man whose lifetime practice of misanthropy is nearing the reward of ultimate perfection."
   Understand "dr" as Doctor Kilpatient.
   The node of Doctor Kilpatient is doctor-node.
   The ask-suggestions are{ self-suggestion, the weather }.
   The tell-suggestions are { your symptoms }.
   The other-suggestions are { advice-suggestion }.

   Part 3 - Conversation

   Chapter 1 - Node-Specific Responses

   doctor-node is a closed convnode.
     the tell-suggestions are { yourself }.

   Response for doctor-node when told about yourself:	
     say "[node ill-node]'I'm not feeling too good, doctor,' you say. [/p]'So what's the matter?' he asks, 'are you ill?' [/l]"

   Default response for doctor-node:
     say "[node ill-node]'I'm a busy man, so let's get to the point. Are you ill?' the doctor demands."

   ill-node is a closed convnode.
   The other-suggestions of ill-node are { yes-no-suggestion }.
   The tell-suggestions of ill-node are { your symptoms }.

   Response for ill-node when saying yes:
     say "[node symptom-node]'Yes, that's why I'm here, doctor,' you tell him. [/p]'So what exactly is the matter?' the doctor wants to know."

   Response for ill-node when saying no:
     say "'No, I just...' you begin. [/p]'Then kindly don't waste my time.' the doctor snaps, 'Goodbye!'";
     end the story finally saying "You have been shown the door".

   Response for ill-node when told about your symptoms:
     say "[remove your symptoms tell suggestion]'Let's take this one step at a time,' he interrupts you, 'Now tell me, are you ill or not, yes or no?'"

   Default response for ill-node:
    say "'Come now, I asked you a simple enough question,' he replies, 'Are you ill, yes or no?'"

   Node-continuation rule for ill-node:
     if a random chance of 1 in 2 succeeds, say "'I haven't got all day,' Dr Kilpatient complains, 'So I'd appreciate it if you would answer my question: are you ill?'"

   symptom-node is a closed convnode.
   The tell-suggestions are { your symptoms }.

   Response for symptom-node when told about your symptoms:
     say "'Well, doctor, I've got this terrible headache, my back's killing me, I'm having trouble walking, and I've got this strange lump on my arm,' you say. [/p][node help-node]'Don't worry,' he replies, 'You'll be dead within the week, and then it won't hurt any more. Now, is there anything else I can help you with?' [/l]"

   Default response for symptom-node:
    say "'No, no, no, don't try to change the subject, just tell me your symptoms!' he interrupts you."

   help-node is a convnode.
   the other-suggestions of help-node are { yes-no-suggestion }.

   response for help-node when saying no:
    say "'No, I think you've been quite helpful enough, doctor,' you reply. [/p]'I do my best,' he replies dryly."

   response for help-node when saying yes:
    say "'Well, yes, I was hoping for something a bit more positive,' you reply. [/p]'I'm not in the business of hope,' he snorts. [/l]"

   Chapter 2 - General Responses

   response for kilpatient when asked for "advice":
    say "[remove advice-suggestion other suggestion]'Can't you give me any advice about how to dull the pain - or stay alive - or anything useful like that?' you ask. [/p]'Pain is good for the soul. So is death. Count yourself fortunate,' he replies. [/l]"

   response for kilpatient when asked about kilpatient:

Quip-Based Conversation
=======================

**Author:** Michael Martin | **Version:** 5.1

An extension to Reactable Quips to allow for more traditional menu-based
conversation.

**Basic example:** Joe Schmoe Revisited

A reimplementation of David Glasser's PHTALKOO.H example, with additions showing
interaction with Reactable Quips and independent conversations.

.. code-block:: inform7

   The story headline is "An Interactive Revisiting of the phtalkoo.h Test".
   Include Quip-Based Conversation by Michael Martin.
   Use no scoring and no deprecated features.

   Chapter 1 - The Setup

   When play begins, say "Joe Schmoe is yor frend!"

   Joe Schmoe's Place is a room.  "You are in Joe Schmoe's place."

   Joe Schmoe is a man in Joe Schmoe's Place.  The description is "This is Joe. It's yor frend!"  The litany of Joe Schmoe is the Table of Joe Comments.

   The greeting of yourself is selftalk.

   Casting Xyzzy is an action applying to nothing.  Understand "xyzzy" as casting xyzzy.  Carry out casting xyzzy: deliver the xyzzy quip; run a conversation on the Table of Magic Followups.

   Chapter 2 - The Script

   Section 1 - The Text

   Table of Quip Texts (continued)
   quip		quiptext
   selftalk		"Talking to yourself is not particularly fun."
   who-am-i	"'My name is Joe Schmoe and Inform hates me.'"
   why-hate	"'I tried to compile a game and it gave me 40 Problem messages.'"
   yay-inform	"'Thanks so much! You're the greatest!'"
   hate-you	"'I hate you!'[paragraph break] Joe kills you."
   hate-you-2	"'I hate you!'[paragraph break] Joe kills you."
   hate-you-3	"'I hate you!'[paragraph break] Joe kills you."
   hate-pedants	"'I hate pedants!'[paragraph break] Joe kills you."
   yay-monkeys	"'Of course I like monkeys.'"
   yay-you		"'Now we can be friends!'"
   say-nothing	"You decide not to say anything after all."
   ehn-apes	"'Apes are OK, I guess.'"
   ehn-lemurs	"'I don't really have an opinion on lemurs.'"
   xyzzy		"What's the other magic word?"

   Table of Joe Comments
   prompt					response	enabled
   "Who are you?"				who-am-i	1
   "Why does Inform hate you?"		why-hate	0
   "You probably just left out a semi-colon."	yay-inform	0
   "I don't care."				hate-you	0
   "Ha, ha. Inform hates you."		hate-you-2	0
   "Do you like a monkey?"			yay-monkeys	1
   "Only crazy people like monkeys."		hate-you-3	0
   "No, I said 'a monkey', not 'monkeys'."	hate-pedants	0
   "I like monkeys too."			yay-you		0
   "Say nothing"				say-nothing	1

   Table of Quip Followups (continued)
   quip		option			result
   yay-monkeys	"What about apes?"	ehn-apes
   yay-monkeys	"What about lemurs?"	ehn-lemurs

   Table of Magic Followups
   prompt					response	enabled
   "PLUGH"					yay-you		1
   "There are at least two; which one?"	hate-pedants	1

   Section 2 - Dialogue affects itself

   After quipping when the current quip is who-am-i:
   	enable the why-hate quip;
   	enable the hate-you quip.

   After quipping when the current quip is why-hate:
   	disable the hate-you quip;
   	enable the hate-you-2 quip;
   	enable the yay-inform quip.

   After quipping when the current quip is yay-monkeys:
   	enable the hate-you-3 quip;
   	enable the hate-pedants quip;
   	enable the yay-you quip.

   After quipping when the current quip is say-nothing:
   	enable the say-nothing quip;
   	terminate the conversation.

   Section 3 - Dialogue affects the game

   After quipping when the current quip is hate-you: end the story saying "You have died".
   After quipping when the current quip is hate-you-2: end the story saying "You have died".
   After quipping when the current quip is hate-you-3: end the story saying "You have died".
   After quipping when the current quip is hate-pedants: end the story saying "You have died".
   After quipping when the current quip is yay-inform: end the story finally saying "You have won".
   After quipping when the current quip is yay-you: end the story finally saying "You have won".

   Section 4 - Tests

   test me with "talk to me / x joe / talk to joe / 1 / x me / 1 / repeat / 3 / x me / 1 / 1".
   test xyzzy with "xyzzy / 1".

####################################
General Utilities & Miscellaneous
####################################

Bulky Items IT
==============

**Author:** Leonardo Boselli | **Version:** 2

Basato sull'espansione Version 2 of Bulky Items by Juhana Leinonen.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Patrollers IT
=============

**Author:** Leonardo Boselli | **Version:** 11

Based on Version 11 of Patrollers by Michael Callaghan.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Questions IT
============

**Author:** Leonardo Boselli | **Version:** 4

Basato su Version 4 of Questions by Michael Callaghan.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Title Page IT
=============

**Author:** Leonardo Boselli | **Version:** 2

Fornisce un pannello introduttivo al gioco, con un menù, la possibilità di
caricare e ricominciare, una citazione e (in Glulx) una figura. Semplicemente
tradotto dall'originale.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

####################################
Multimedia: Graphics & Sound
####################################

Multiple Sounds
===============

**Author:** Massimo Stella | **Version:** 3

Provides facilities for the basic reproduction of multiple-channel audio with
loops under Glulx.

**Basic example:** Rainforest

Shows how to use multiple sounds effects to mimic a natural environment.

.. code-block:: inform7

   Include Multiple Sounds by Massimo Stella.

   The Swamp is a room. The description is "A beautiful mirror of water is in front of your eyes while behind you there are the tallest trees you've ever seen. You can hear the sound of some frogs in the distance."

   Sound of frogs is the file "Frogs.ogg". 
   Sound of water is the file "Water.ogg".
   Sound of wind is the file "Storm.ogg".

   When play begins:
   	set the background volume to 2;
   	play the sound of frogs in background;
   	set the foreground volume to 3;
   	play the sound of water in foreground with loop;
   	create the midground channel;
   	set the raw midground volume to 10000;
   	play the sound of wind in midground.

#######################################
Objects, Actions & Physical Interaction
#######################################

Alternatives
============

**Author:** Eric Eve | **Version:** 3

Allows checking the presence of an object or value in a set of objects or values
with new either/or and neither/nor phrases. e.g., 'If the noun is either the
carrot or the potato:', or 'Instead of eating something when the noun is neither
the cake nor the pudding:'

**Basic example:** Paintshop Blues

Experimenting with the actions the player is prepared to perfom on differently
coloured objects.

.. code-block:: inform7

   Book 1 - World Model

   Include Alternatives by Eric Eve.

   colour is a kind of value. The colours are red, orange, yellow, green, turquoise, blue, purple, black and white.

   A chromatinon is a kind of thing. A chromatinon has a colour. 

   before printing the name of a chromatinon:
     say "[colour of the item described] ";

   Understand the colour property as describing a chromatinon.

   Painting is an action applying to one thing and one colour.

   Understand "paint [something] [colour]" as painting.

   Check painting something when the noun is not a chromatinon:
      say "I'm afraid that can't be recoloured." instead.

   Check painting a chromatinon when the colour of the noun is the colour understood:
     say "But [the noun] is already [the colour understood]!"

   Carry out painting a chromatinon:
     Now the colour of the noun is the colour understood.

   Report painting a chromatinon:
     say "Okay -- it's now [a noun]."

   Book 2 - Scenario

   Part 1 - Objects

   The Experimental Paintshop is a room.
   "This is where you can test the effect of colour on your highly colour-sensitive mind."

   The ball is a blue chromatinon in the Experimental Paintshop.

   The pencil is a black chromatinon in the Experimental Paintshop.

   The pen is a red chromatinon in the Experimental Paintshop.

   The table is a supporter in the Experimental Paintshop.

   The china cup is an orange chromatinon on the table.

   The china plate is a white chromatinon on the table.

   Part 2 - Rules

   After taking something when the noun is either the pencil or the pen:
     say "You pick up a writing implement ([a noun], to be precise)."

   After taking the ball when the colour of the ball is either blue or green:
     say "You pick up [the ball]."

   Instead of dropping something when the noun is either the china cup or the china plate:
     say "But it might break if you drop it!"

   After taking inventory when the number of things carried by the player is either 1 or 3 or 5:
     say "You seem to be holding an odd number of things."

   After taking inventory when the number of things carried by the player is neither 0 nor 1 nor 3 nor 5:
     say "You are carrying an even number of objects."

   Instead of dropping something when the colour of the noun is either turquoise or blue or purple:
     say "But it's so pretty -- [the colour of the noun] is one of your favourite colours!"

   Instead of taking something when the colour of the noun is either black or white:
     say "But it's so plain!"

   Before eating something when the colour of the noun is neither red nor orange nor green nor white:
     say "Whoever heard of [colour of the noun] food? [A noun] can't possibly be edible!" instead.

   Test me with "eat ball/take plate/paint plate red/eat plate/drop plate/take pencil/paint pencil orange/take pencil/i/take ball/drop ball/i/take pen/paint pen purple/eat pen/drop pen/i"

Autotaking
==========

**Author:** Mike Ciul | **Version:** 1

Implicit taking of noun or second noun that may be invoked by (or used as) a
check rule.

**Basic example:** Butterfingers

Making sure the "attacking it with" action always uses a held weapon.

.. code-block:: inform7

   Include Autotaking by Mike Ciul.

   Attacking it with is an action applying to two things.

   Understand "attack [something] with [something]" as attacking it with.

   The must hold the second noun rule is listed first in the check attacking it with rulebook.

   Check attacking something with something:
   	If the noun is not a person:
   		say "You do very little damage to [the noun].";
   		stop the action.

   Check attacking the player with something:
   	say "You wound yourself slightly, but the pain causes you to stop.";
   	stop the action.

   Carry out attacking something with something:
   	Now the second noun is in the location.

   Report attacking something with something:
   	say "With a mighty yell, you swing [the second noun] at [the noun]. Unfortunately, it slips from your sweaty fingers and falls to the ground."

   Arena is a room.

   The gladiator is a man in Arena.

   There is a sword in Arena. There is a big rock in Arena.

   Instead of taking the big rock, say "You strain to lift the rock, but it's too heavy for you."

   test me with "i/attack rock with sword/i/attack me with sword/attack gladiator with sword/g/attack gladiator with rock"

Basic Plans
===========

**Author:** Nate Cull | **Version:** 3.3

A library of basic relations, actions and plans for Planner.

**Basic example:** Alchemy

A demo game showing use of these basic actions.

.. code-block:: inform7

   [This is a demo game for Planner.]

   The release number is 2.
   The story creation year is 2006.
   The story headline is "An Interactive Demonstration"

   Include Basic Plans by Nate Cull.

   The Laboratory is a room. The description of the Laboratory is "A chaos of glassware, dark sigils, spellcasting apparatus sprawled in disgusting confusion -- in other words, a perfectly normal research lab. A stone archway leads east and another south."

   The Library is east of the Laboratory. The description of the Library is "The stony walls are racked with square miles of parchment volumes." 

   A curiously carved table is a supporter in the Library.

   A rosewood bench is a supporter in the laboratory. "A rosewood bench, scarred and burned by years of incantations, fills half of the room."

   An iron crucible is an open container on the rosewood bench. "Bob's crucible bubbles merrily on the bench."

   A cupboard is a closed openable container in the laboratory. "A cupboard of great antiquity quietly blends into the corner shadows."

   A plastic bag is a closed transparent portable openable container on the carved table.

   A Chinese puzzle box is a locked lockable closed openable portable container in the plastic bag.

   A pinch of ginger is a portable thing in the puzzle box.

   A wicker basket is an open container in the cupboard.

   An onion, a tomato, a stick of celery, a lemon and a banana are in the wicker basket.

   Broth is a thing.

   The basic putting things in containers rule does nothing when the desired relation is being-in and the desired param1 is broth and the desired param2 is the crucible.

   Planning when the desired relation is being-in and the desired param1 is broth and the desired param2 is the crucible:
   	plan 1;
   	suggest being-in with the onion and the crucible;
   	suggest being-in with the celery and the crucible;
   	suggest being-in with the banana and the crucible;
   	suggest being-in with the ginger and the crucible;

   To decide whether soup is brewing:
   	if the onion is not in the crucible, decide no;
   	if the celery is not in the crucible, decide no;
   	if the banana is not in the crucible, decide no;
   	if the ginger is not in the crucible, decide no;
   	decide yes;


   Every turn when soup is brewing:
   	if the crucible is visible, say "The crucible simmers; the contents meld into a rich pungent vegetable broth.";
   	repeat with item running through things in the crucible begin;
   		now item is nowhere;
   	end repeat;
   now broth is in the crucible;

   The Alcove is a room.

   The Alcove is south of the Laboratory. The description of the Alcove is "A tiny niche carved out of the stone, which opens out to the north."

   A brass hook is a supporter in the Alcove. "Screwed into the stonework with grim determination is a shiny brass hook." The brass hook has carrying capacity 1.

   A silver key is on the brass hook. The matching key of the Chinese puzzle box is the silver key.



   Bob is a person in the laboratory. "The mighty wizard Bob potters around his domain."

   The description of Bob is "Bob is carrying [if bob carries anything][list of things carried by bob][otherwise]nothing[end if]."

   The basic dropping objects in rooms rule does nothing when the desired relation is being-in and the desired param1 is a person.

   Every turn:
   	have Bob plan an action for being-in with broth and the crucible;

   Rule for deciding the concealed possessions of Bob:
   	decide no;



   Section - Custom Actions

   [Asking a person for an object is an alternative plan for getting hold of an object. It's the sort of strategy that would only be appropriate in some genres, so it's not in Basic Plans.]

   Doing-asking-for is a planning-action.

   Planning-acting when the planned action is doing-asking-for:
   	try the planning actor trying asking the planned param1 for the planned param2;

   Planning rule when the desired relation is being-touchable-by and the desired param2 is the planning actor and a person (called the owner) encloses the desired param1:
   	plan 1;
   	suggest being-touchable-by with the owner and the planning actor;
   	suggest doing-asking-for with the owner and the desired param1;


   The block giving rule does nothing when the second noun is Bob.


   Section - Custom Messages

   [The 'action success flag' trick we use is a bit of a nasty hack. There is probably a better way to find out if an action succeeds, but I don't know it yet. For the moment we use this, but it only gets set if an 'after' rule runs, which means if we use 'instead' to block the action, we need to set it manually. We should probably have a phrase for this, but it's so ugly there's likely to be a more permanent solution anyway.]

   Instead of Bob trying asking the player for something:
   	say "'I say, old chap,' mutters Bob. 'Do be a sport and give me [the second noun].'";	
   	now the action success flag is 1;

   Planning-failure:
   	say "Bob scratches his beard and looks perplexed.";

   Planning-success:
   	end the story finally saying "You have witnessed the Making of Soup";	

   Planning-acting-failure:
   	say "'Arr, that didn't work,' says Bob. 'Reality be getting a mite thin.'";

   Report Bob trying opening the cupboard for the first time:
   	say "'Aslan sesameslan!' says Bob, flinging the cupboard doors wide open to reveal [list of things in the cupboard].";
   	stop the action;

   [Another nasty hack just to get a nice message when Bob takes something from a container rather than from the room. Must be a better way to do this.]

   The previous take holder is an object that varies.

   Before Bob trying taking something:
   	now the previous take holder is the holder of the noun;

   Report Bob trying taking something:
   	if the previous take holder is not a room begin;
   		say "Bob takes [the noun] from [the previous take holder].";
   		stop the action;
   	end if;

Bulk Limiter
============

**Author:** Eric Eve | **Version:** 9

Containers and actors that limit their contents by bulk

**Basic example:** The Basket, the Bricks and the Spoon

Putting things in a container with not quite enough room for them all, and
carrying things without quite enough arms for them all.

.. code-block:: inform7

   Include Bulk Limiter by Eric Eve

   The bulk capacity of a person is normally 10.

   The Kitchen is a room. "The only furniture of interest is the table." 
   A table is a scenery supporter in the kitchen. 
   A small spoon is on the table.

   A large hamper is in the kitchen. The bulk is 100.

   On the table is a container called the wicker basket.

   A brick is a kind of thing. The bulk of a brick is normally 5. Two bricks are here.

   Understand "put [things] in [something]" as inserting it into.	

   Test me with "Put bricks in basket/put spoon in basket/take brick/put spoon in basket/put brick in basket/put spoon in basket/take brick/take spoon/take hamper".

Bulky Items
===========

**Author:** Juhana Leinonen | **Version:** 3

Bulky items that can be carried only if the player is not carrying anything
else.

**Basic example:** Smarter TAKE ALL

Excluding bulky items from TAKE ALL and informing the player about it.

.. code-block:: inform7

   Include Bulky Items by Juhana Leinonen.

   Living room is a room. A television is in the living room. It is bulky. A remote control is in the living room.

   Rule for deciding whether all includes bulky things:
   	it does not.

   Every turn when multiple taking:
   	if a bulky handled thing is in the location and the current action is taking:
   		say "(bulky items, i.e. [the list of bulky handled things in the location], were ignored)[line break]";

   Test me with "take all/take television/drop all/take all".

Conversation Framework
======================

**Author:** Eric Eve | **Version:** 12

A framework for conversations that allows saying hello and goodbye, abbreviated
forms of ask and tell commands for conversing with the current interlocutor, and
asking and telling about things as well as topics.

**Basic example:** The Ring, the Gardener and the the Maid

Putting Conversation Framework through its paces.

.. code-block:: inform7

   Book 1 - Setup

   Include Conversation Framework by Eric Eve.

   Instead of giving something to someone, try showing the noun to the second noun.	

   jim-knows-ring is a truth state that varies. jim-knows-ring is false.

   Book 2 - Scenario

   Chapter  1 - The Dining Room

   The Dining Room is a room. "Most of the room is taken up with a large wooden dining table. The only way out is to the south."

   The large wooden dining table is a supporter in the Dining Room. It is scenery.

   On the large wooden dining table is a gold ring. It is wearable.

   Chapter 2 - Sarah

   Sarah is a woman in the Dining Room. "Sarah is [if Sarah is the current interlocutor]standing by the table, looking at you[otherwise]busily polishing the table[end if]." The description is "She's a pretty young brunette."

   Understand "pretty" or "young" or "woman" or "brunette" as Sarah.

   After saying hello to Sarah when the greeting type is explicit:
   say "'Hello there!' you say.[paragraph break]'Hello!' she replies with a grin."

   After saying hello to Sarah when the greeting type is implicit:
   say "'Excuse me', you say.[paragraph break]'Yes?' she asks."

   Asking Sarah about something is Sarah-chatting.
   Telling Sarah about something is Sarah-chatting.

   After quizzing Sarah about Sarah:
     say "'How are you, Sarah?' you ask.[paragraph break]'I'm fine, thank you.' she assures you."

   After quizzing Sarah about the gold ring when the gold ring is on the table:
    say "'Is that your ring?' you ask, nodding towards the table.[paragraph break]'No, I found it on the floor.' she tells you."

   After quizzing Sarah about the gold ring when the player has the gold ring:
     say "'You don't mind if I take this ring then?' you ask.[paragraph break]'As long as you're only taking it to return it to its owner.' she replies."

   After Sarah-chatting when the topic understood matches "[weather]":
     say "'Lovely weather today, don't you think?' you remark.[paragraph break]'Don't you have anything more interesting to talk about?' she complains."

   After quizzing Sarah about the dining table:
     say "'Have you been polishing that table long?' you ask.[paragraph break]'Long enough.' she replies."

   After saying goodbye to Sarah when the farewell type is explicit:
     say "Cheerio then,' you say.[paragraph break]'See you,' she replies."

   After quizzing Sarah about Jim:
     say "'What do you think of Jim?' you ask.[paragraph break]'That's for me to know and you to find out,' she replies mysteriously."

   After informing Sarah about Jim when the Garden is visited:
     say "'Well, Jim seems to be hard at work weeding,' you remark.[paragraph break]'He should try getting this table clean!' she replies."

   After informing Sarah about the flower beds:
     say "'The flower beds are coming on nicely,' you remark.[paragraph break]'I'm sure Jim knows his job,' she replies."

   After saying goodbye to Sarah when the farewell type is implicit:
     say "Sarah goes back to polishing the table."

   After conversing when the noun is Sarah:
     say "She mutters something incomprehensible under her breath."

   Understand "weather" or "the weather" as "[weather]".

   Chapter 3 - The Hall

   The Hall is south of the Dining Room. "This large bare hall has exits to north and east."

   Chapter 4 - The Garden

   The Garden is east of the Hall. "The front lawn is surrounded by flower beds. The way back into the hall is to the west."

   Some flower beds are scenery in the Garden. The description is "They are shaping up nicely." 

   Chapter 5 - Jim

   Jim is a man in the Garden. "Jim is [if jim is the current interlocutor]standing by one of the flower beds, talking to you[otherwise]bent over over of the beds, busily weeding[end if]."

   After saying hello to Jim when the greeting type is explicit:
     say "'Hello there, Jim!' you say.[paragraph break]Jim painfully straightens himself, hand on hip, then focus on you, grunting, 'Good afternoon!'"

   After saying hello to Jim when the greeting type is implicit:
     say "You attract Jim's attention with a cough, and he straightens painfully to hear what you have to say."

   After informing Jim about the gold ring when the gold ring is on the dining table:
     say "'I saw a gold ring on the dining table: is it yours?' you ask.[paragraph break]'It might be - can't say till I see it,' he grunts."

   Instead of informing Jim about the gold ring when the player has the gold ring:
     try showing the gold ring to Jim.

   Instead of showing the gold ring to Jim:
   if jim-knows-ring is true begin;
   	 say "'You're quite sure that ring isn't yours?' you ask.[paragraph break]'Quite sure,' he affirms.";
   otherwise;
     	now jim-knows-ring is true;
     	say "'Is this your ring?' you ask.[paragraph break]Jim takes one look at him and shakes his head, 'Nah, I wouldn't be seen dead wearing a poncy thing like that!' he declares.";
   end if.
   	 

   Instead of quizzing Jim about the gold ring:
     try informing Jim about the gold ring.

   After informing Jim about Sarah:
     say "'Sarah seems to be hard at work in the dining room,' you remark.[paragraph break]'Aye, she's a hard-working girl is that one,' Jim concurs."

   After quizzing Jim about Sarah:
     say "'What do you think of Sarah?' you inquire.[paragraph break]'She's a bonny lass, that one!' he declares."

   After telling Jim about "[weather]":
     say "'Nice weather today!' you remark.[paragraph break]'Bit hot for working in, if you ask me,' he replies, mopping his brow."

   After asking Jim about "[weather]":
     say "'Do you reckon this weather will hold?' you ask.[paragraph break]'Nah, there'll be storms tonight, you mark my words,' he tells you."

   After conversing when the noun is Jim:
     say "Jim mutters darkly under his breath."

   After saying goodbye to Jim when the farewell type is explicit:
     say "'Well, goodbye then!' you say.[paragraph break]'Goodbye,' he grunts, turning back to the flower bed."

   After saying goodbye to Jim when the farewell type is implicit:
     say "Jim waves at you and then returns to his weeding."

   Book 3 - Testing - not for release

   Test sarah with "Sarah, hello/a table/a weather/a ring/a jim/a love/a herself/bye/s"

   Test jim with "e/ask jim about ring/ask jim about sarah/t sarah/a weather/t weather/w"

   Test end with "hello/n/t jim/take ring/a ring/s/e/hello/t ring/a ring/jim, bye"

   Test me with "test sarah/test jim/test end"

Dynamic Objects (for Glulx only)
================================

**Author:** Tara McGrew | **Version:** 9.0.0

Provides the ability to create new objects during game play.

**Basic example:** The Cubbins Effect

Creating a new hat every time the player removes the one he's wearing.

.. code-block:: inform7

   Include Dynamic Objects by Tara McGrew.

   King Derwin's Court is a room. "You have been summoned here for the crime of failing to remove your hat in the king's presence."

   A hat is a kind of thing.

   A hat style is a kind of value. The hat styles are red, blue, green, yellow, white, black, brown, zebra-striped, tall, pointy, short, gray, pink, fuzzy, rainbow-colored, and feathered.

   A hat has a hat style. Before printing the name of a hat, say "[hat style] ". Understand the hat style property as describing a hat.

   The player wears a hat which is red.

   Instead of taking off a hat which is worn by the player:
   	now the noun is in the location;
   	if 500 hats are in the location:
   		say "You remove [the noun] and drop it. It seems that was the last one!";
   		end the story finally saying "You have won";
   	otherwise:
   		let the new hat be a new object cloned from the noun;
   		now the player is wearing the new hat;
   		say "You remove [the noun] and drop it, only to find another hat upon your head -- a [hat style of the new hat] one."

   After cloning a new object from a hat (called the original hat):
   	while the hat style of the new object is the hat style of the original hat:
   		now the hat style of the new object is a random hat style.

   Rule for printing a number of hats (called the particular headwear):
   	say "[listing group size in words] [hat style of the particular headwear] hats".

   Test me with "remove hat / remove hat / remove hat / i / look".

Editable Stored Actions
=======================

**Author:** Ron Newcomb | **Version:** 10

This extension extends section 12.20 of Writing With Inform. The individual
parts of a stored action -- actor, noun, second noun, action name -- can be
changed directly. Also exposes new parts: request, text, participle,
preposition, number, and each kind of value.

**Basic example:** The Ultimate Puzzle Solution

A kind of value's not-so-kind example

.. code-block:: inform7

   Include Editable Stored Actions by Ron Newcomb.

   The backyard is room.  A Rubik's cube is a thing carried by the player.

   Feet are a kind of value. 10' specifies feet.

   Throwing it is an action applying to one object and one feet.
   Understand "throw [something] [feet]" as throwing it.

   Pent-up frustration is a stored action that varies.

   Report throwing it:
   	now pent-up frustration is the current action;
   	change the second feet part of pent-up frustration to the feet understood plus 10';
   	say "Although [the current action] was all you intended, you find yourself [pent-up frustration] instead."

   Test me with "throw rubik's cube 30['] "

Enterable Underside
===================

**Author:** Gavin Lambert | **Version:** 2.0.221220

Adds the ability to enter 'under' some object, such as hiding under a bed.

**Basic example:** A Nice Picnic

Spreading out a picnic blanket underneath a tree.

.. code-block:: inform7

   Include Enterable Underside by Gavin Lambert.

   Picnic Area is a room.  "A bright open area close to a large tree.  [if the blanket is carried]You can either set up your picnic out in the open or under the tree.[end if]".
   A large tree is scenery in Picnic Area.  The description is "An oak, you think."
   An underside called under#tree is part of the tree.  It is enterable and transparent.  The preposition is "beneath".
   The verb to go beneath means the reversed containment relation.  The entering preposition of under#tree is verb go beneath.

   The player carries a large checkered blanket and a small picnic basket.  The blanket is an enterable supporter.  The basket is a locked container.

   Understand "sit under/beneath [tree]" as entering underneath.

   Test me with "put blanket under tree / sit on blanket / drop basket / l / exit / exit".

Flexible Action Requirements
============================

**Author:** Mike Ciul | **Version:** 1

Overrides carrying requirements for specific actions, and provides more nuanced
carrying and touchability requirements when needed.

**Basic example:** "Mange Tout"

A blancmange that can't be taken but can be eaten, and tennis fans who can't be
touched but can be heard.

.. code-block:: inform7

   Include Flexible Action Requirements by Mike Ciul.

   Wimbledon Stadium is a room. A giant blancmange is a fixed in place edible thing in Wimbledon Stadium.

   The fans are a plural-named person in Wimbledon.

   Accessibility rule when the fans must be touched:
   	say "The fans are too far away.";
   	stop the action;

   Instead of listening to the fans when the blancmange is off-stage:
   	say "A tremendous roar of jubilation washes over you.";
   	end the story finally saying "You have won the match."

   Instead of listening to the fans:
   	say "The crowd is hushed with terror and anticipation.";

   Eating is flexible about carrying the noun;
   Listening is flexible about touching the noun;

   Test me with "listen to fans/eat fans/take blancmange/eat blancmange/listen to fans"

Gender Speedup
==============

**Author:** Nathanael Nerode | **Version:** 3.0.220524

When using Gender Options, clean up some I6 internals with functions related to
gender which are irrelevant to English or rendered obsolete with Gender Options.
Since these are called in the depths of ListWriter this should slightly improve
speed. Not included in Gender Options due to likely interference with other
extensions. Requires Gender Options. Will not work with languages with gendered
plurals. Tested with Inform 10.1.

**Documented usage:**

.. code-block:: inform7

   Use OMIT_UNUSED_ROUTINES of 1.

Implicit Actions
================

**Author:** Eric Eve | **Version:** 13.1

Provides implicit taking, opening, closing, locking and unlocking actions for a
variety of cases where this makes for smoother game play. The extension also
defines phrases which make it easy to define additional implicit actions if
desired. Version 11 can be used with Locksmith by Emily Short (although Implicit
Actions covers most of what Locksmith does, and in most cases it will be better
to use Implicit Actions without Locksmith). Requires Version 8.1 (or above) of
Text Capture by Eric Eve.

**Basic example:** Football Practice

Defining a new implicit action.

.. code-block:: inform7

   Include Implicit Actions by Eric Eve.

   Part 1 - Define the Implicit Drop Activity

   implicitly dropping something is an activity.

   rule for implicitly dropping something (called the held-thing) :
      initialize the implicit action;
      silently try dropping the held-thing;  
      finish the implicit action with participle "dropping" infinitive "drop" object "[the held-thing]" and condition (whether or not the held-thing is not carried).

   Part 2 - The Kicking Action

   kicking is an action applying to one thing.
   Understand "kick [something]" as kicking.

   Precondition for kicking something that is carried:
      carry out the implicitly dropping activity with the noun;
      if the noun is carried and implicit action attempted is true, stop the action.

Keyword Interface
=================

**Author:** Aaron Reed | **Version:** 9.0.1

This extension emulates Blue Lacuna's emphasized keyword system for simplifying
common IF input. Nouns, directions, and topics can be typed without a verb to
examine, go, or discuss. Works with Glulx or z-code.

**Basic example:** Sense of Direction

A simple usage of the extension to print bold compass directions.

.. code-block:: inform7

   Include Keyword Interface by Aaron Reed.

   Object keyword highlighting is false. The style of direction-word is keyword-bold-style.

   Labyrinth is south of Passage and west of Halls. Halls is south of Dungeon and west of Pit. Pit is south of Harrows. Harrows is east of Dungeon and south of Caverns. Dungeon is east of Passage and south of Abyss. Passage is south of Abattoir. Abattoir is west of Abyss and north of Passage. Abyss is west of Caverns.   

   After looking: try listing exits.

   [This is the correct order for test commands, but for some reason they are running in reverse]
   [Test me with "north / north / east / south / south / east / north / north / west / west / south / south".]
   [So test with this instead:]
   Test me with "south / south / west / west / north / north / east / south / south / east / north / north".

Large Game Speedup
==================

**Author:** Nathanael Nerode | **Version:** 6.0.220524

Performance improvements for games with many objects, or with nested loops over
objects, by avoiding looping over all objects.

**Basic example:** Four Hundred Things

A small game with a lot of stuff.

.. code-block:: inform7

   LOOK in Kitchen:
   without: 1013460 cycles (103.647 ms C, 1918 ms JS)
   with: 77386 cycles (20.791 ms C, 193 ms JS)

   JUMP
   without: 54474 cycles (18.451 ms C, 117 ms JS)
   with: 43752 cycles (16.606 ms C, 103 ms JS)

   EXAMINE MIRROR in Kitchen
   without: 75159 cycles (20.602 ms C, 178 ms JS)
   with: 45975 cycles (17.757 ms C, 104 ms JS)

   LOOK in Game Room
   without: 1025383 cycles (105.147 ms C, 1844 ms JS)
   with: 105354 cycles (22.663 ms C, 193 ms JS)

Limited Implicit Actions
========================

**Author:** Eric Eve | **Version:** 3.0.1

A cut-down version of Implicit Actions for use where code size may be restricted
and the full functionality of Implicit Actions is not needed. Compatible with
Locksmith by Emily Short.

**Basic example:** Balancing Act

Putting Limited Implicit Actions through its basic places.

.. code-block:: inform7

   Include Limited Implicit Actions by Eric Eve.

   The Old Theatre is a room.
   "Most of the seating has been stripped out, although the stage remains. The way out to the Prop Store lies east."

   The stage is a scenery enterable supporter in the Theatre.

   The wooden chair is a portable enterable supporter in the Theatre.
   "A lone wooden chair sits facing the stage."

   The Prop Store is east of the Theatre.
   "The Prop Store has been stripped bare, apart from the cupboard set into one wall. The way back to the Theatre lies west."

   The prop cupboard is a scenery openable closed container in the Prop Store.

   The small stool is a portable enterable supporter in the prop cupboard.

   A glass jar is a transparent openable closed container in the prop cupboard.

   A small red ball is in the glass jar.

   Test me with "put chair on stage/sit on chair/e/look in cupboard/take stool/take jar/x jar/take ball/close cupboard/drop jar/put jar in cupboard/put cupboard on stool/w/put stool on chair/sit on stool/e"

Modified Timekeeping
====================

**Author:** Daniel Stelzer | **Version:** 1

Changes the one-minute-per-turn rule to account for failed and implicit actions.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Object Descriptors
==================

**Author:** Peter Orme | **Version:** 3

**Basic example:** The Den

just describing some things

.. code-block:: inform7

   Include Object Descriptors by Peter Orme.

   The Den is a room.

   The wooden chest is a container in the den. It is closed, openable.

   Mrs Benson is a woman in the den.

   the marble bench is a supporter in the den. It is fixed in place. 

   the portal is a door. It is outside from the den.

   the rat king is an animal in the den. The indefinite article is "a". it is plural-named.

   The laser slicer is a switched off, unlit device in the den.

   after switching on the laser slicer: 
   	now the laser slicer is lit;
   	continue the action.

   after switching off the laser slicer: 
   	now the laser slicer is unlit;
   	continue the action.

   [Let's also introduce a new Kind of Thing. Custom properties won't break anything, but they won't be described unless we add an object descriptor rule for it]

   a wooz is a kind of thing. a wooz can be floppy or stiff. 

   an Object Descriptor rule for a wooz (called item):
   	if the item is floppy, add "floppy" to the descriptor list;
   	if the item is stiff, add "stiff" to the descriptor list;

   There is a floppy edible wooz called a spongy cake in the lab.

   when play begins:
   	repeat with item running through things:
   		say "[item] - [the object descriptors of the item].";

Objects Matching Snippets
=========================

**Author:** Mike Ciul | **Version:** 1

list of things identified with the topic understood

**Basic example:** Exclamations

Creates a new action that can be parsed from the command "[someone],
[something]"

.. code-block:: inform7

   Include Objects Matching Snippets by Mike Ciul.

   Exclaiming it to is an action applying to two visible things.
   Report exclaiming it to: say "You say '[noun]' to [the second noun]."

   An exclamation is a kind of thing. Hello is an exclamation.

   Check answering someone that:
   	Let item be the most likely thing identified with the topic understood;
   	If item is a thing:
   		instead try exclaiming item to the noun;
   	Let item be the most likely thing named in the topic understood;
   	if something matched:
   		say "Your command did not exactly match anything you can say, but [the list of likeliest things named in the topic understood] matched part[if item is nothing]s[end if] of it.";
   		stop the action.

   Test is a room. Bob is a man in Test.

   Test me with "say hello to bob/bob, hello how are you Bob"

Optimized Epistemology
======================

**Author:** Andrew Plotkin | **Version:** 1.2

Keeping track of what the player character knows and sees.

**Basic example:** Contemplation

Thinking about things that are known

.. code-block:: inform7

   Include Optimized Epistemology by Andrew Plotkin.

   Part  1 - Thought Mechanics

   Thinking about is an action applying to one visible thing.

   Understand "think about [any thing]" as thinking about.
   Understand "think about [any known thing]" as thinking about.

   Report thinking about something unknown:
     say "[no thoughts]"

   Report thinking about something known:
     say "[the thought of the noun][paragraph break]"

   A thing has a text called thought.

   Pondering is an action applying to one topic.

   Understand "think about [text]" as pondering. [otherwise we get an ugly response to THINK ABOUT FOO etc.]

   Report pondering:
     say "[no thoughts]"

   To say no thoughts:
      say "You have no thoughts on that subject right now."

   Part  2 - Scenario

   The player wears a watch.

   The Study is a Room. "You deliberately keep this room as bare as possible, to prevent material objects distracting you from your thoughts. The two essential objects that remain are a comfortable armchair and the door out into the hall to the west."

   The comfortable armchair is an enterable scenery supporter in the Study. The description is "It's nothing special, but it looks comfortable enough." The thought is "You think it's a good place to sit and think."
   Understand "arm" or "chair" as the comfortable armchair.

   Report entering the armchair:
   	instead say "You sit down and dream about golf."

   The hall door is an open openable scenery door. The hall door is west of the Study and east of the Main Hall. The thought is "Useful things, doors, you muse: without them it would be so much harder to get from room to room."

   The Golf Dream is scenery. The description is "You have long had a distant dream of playing golf in some paradisaical country club." The thought is "[description of the Golf Dream]".

   After deciding the scope of the player when the player is on the armchair:
   	place the Golf Dream in scope.

   The Main Hall is a Room. "This place is almost as sparsely furnished as the Study which lies to the east."

   The large oak table is a supporter in the Main Hall. "A large oak table abuts one wall." The thought is "You've never given this table much thought, to be honest -- it's just a table, after all."

   A note is on the large oak table. The description of the note is "The note reads: 'To find fame, love, and everlasting happiness, you need to go on the quest of the Great Golden Golf Ball of Destiny.'"
   The thought of the note is "You [if we have examined the note]think it contains an interesting proposition[otherwise]wonder what it says[end if]. "

   Carry out examining the note: now the Great Golden Golf Ball of Destiny is familiar.

   Life is a subject. The thought is "You think [if the golden golf ball is familiar]it has just become a whole lot more interesting[otherwise]it's preferable to the alternative[end if]. "

   Liberty is a subject. The thought is "It's a fine word -- but a slippery concept."
   Understand "freedom" as liberty.

   Love is a subject. The thought is "You [if we have examined the note]think it might be worth questing to find it[otherwise]wonder where it is to be found[end if]. "

   Understand "fame" or "everlasting" or "happiness" as love.

   The Great Golden Golf Ball of Destiny is a thing. The thought is "You wonder what kind of object it can be to offer so much."

   The red box is an open container on the large oak table.
   The red ball is in the red box.

   The green box is a closed openable container on the large oak table.
   The green ball is in the green box.

   The glass box is a closed openable transparent container on the large oak table.
   The crystal ball is in the glass box.

   The widget is in the Main Hall.
   The button is part of the widget.

   The wallpaper is a backdrop. The wallpaper is in the Main Hall.

   Test me with "think about love/think about door/think about golden ball/think about note/think about table/think about life/epistat red ball/epistat green ball/w/think about table/think about note/read note/think about note/think about love/think about golden ball/think about life/epistat golden ball/epistat red ball/epistat green ball/open green box/epistat green ball".

Planner
=======

**Author:** Nate Cull | **Version:** 2.3

A universal goal planner for self-directed NPCs.

**Documented usage:**

.. code-block:: inform7

   'plan 1;'  (this sets the current plan number for 'suggest')
   'suggest <token> with <object 1> and <object 2>;' (you can omit the 'with <object 1>...' and 'and <object 2>' if there is no sensible first or second parameter)

   And just continue with 'suggest...' lines until you're done.

   Each time you call 'suggest...' it will increment an internal step number, and compare this against 'desired step', ignoring the line for all the cases that don't match. This is a bit of a kludge but it's the simplest syntax I've come up with so far. 

   Be aware that rules may interact in unexpected ways unless you put an explicit 'rule succeeds' on the end of yours. Also, the 'Basic Plans' rules may take precedence over more specific rules you write unless you use a procedural rule to make them go away. This may change as I7's rule precedence ordering evolves.

   Check 'Basic Plans' and the demo game 'Alchemy' to see examples of writing plans.

Push Pull Turn
==============

**Author:** Brent Worthington | **Version:** 2

Provides a framework for pushing, pulling and turning.

**Basic example:** Cart Jam

Pulling, Pushing, Turning in action

.. code-block:: inform7

   Include Push Pull Turn by Brent Worthington.

   Supermarket Aisle is a room. "There narrow supermarket aisle has been littered with discarded trolley carts that need to be pulled and twisted free, then pushed safely out of the way."

   A cart is a kind of thing. A cart is usually pushable, pullable and turnable. The red trolley is a cart in the Supermarket Aisle. The green trolley is a cart in the Supermarket Aisle. The yellow trolley is a cart in the Supermarket Aisle.

   The description of a cart is usually "[if the noun is not jammed and the noun is not twisted]The cart has now been freed.[else if the noun is jammed]The cart is jammed.[else]The cart is twisted around, blocking the narrow aisle.[end if]"

   A cart can be jammed. A cart is usually jammed. A cart can be twisted. The yellow trolley is twisted.

   Before taking a cart:
   	say "You can move the cart around, pushing, pulling or turning, but it's too heavy to lift up." instead.

   Check pushing a cart (called the target):
   	if the target is jammed:
   		say "The [target] is jammed in with another trolley." instead;
   	if the target is twisted:
   		say "The [target] is turned the wrong way." instead;
   	if there is a twisted cart (called the blocker) in the Supermarket Aisle:
   		say "The [blocker] is in the way." instead;

   Carry out pushing a cart:
   	now the noun is off-stage;
   	say "You shunt the trolley down the aisle, safely away from the current tangle.";
   	if no carts are in the supermarket aisle:
   		say paragraph break;
   		say "You did it! You cleared the aisle of all the trolleys!";
   		end the story finally.

   Check pulling a cart (called the target):
   	if the target is twisted:
   		say "The [target] is currently turned the wrong way in the aisle to pull." instead;
   	if the target is not jammed:
   		say "The [target] has already been pulled clear." instead.

   Carry out pulling a cart (called the target):
   	now the target is not jammed;
   	say "You pull [the target] clear. [run paragraph on]";
   	if two carts are jammed:
   		say "There are still two carts jammed.";
   	else:
   		now every cart is not jammed;
   		say "The jam has been cleared.";

   Carry out turning a cart (called the trolley):
   	if the trolley is jammed:
   		say "It's too jammed in with the other trolleys to turn." instead;
   	else if the trolley is twisted:
   		say "You turn the trolley around, unblocking the aisle.";
   		now the trolley is not twisted;
   	else:
   		now the trolley is twisted;
   		say "You turn the trolley around, blocking the aisle."

   The shelves are scenery in the supermarket aisle.

   The initial appearance of a cart is usually "The [item described] is [if the item described is twisted and the item described is jammed]jammed with another trolley, and twisted to one side, blocking the aisle[else if the item described is twisted]twisted, blocking the aisle[else if the item described is jammed]jammed with another trolley[else]sitting neatly in the aisle[end if]."

   Test me with "Push shelves / pull shelves / turn shelves / pull yellow / push yellow / push red / turn red / pull green / pull red / turn yellow / push red / push green / push yellow"

Rideable Vehicles
=================

**Author:** Gavin Lambert | **Version:** 1.3.1

Improves how rideable vehicles and animals interact with other supporters.

**Basic example:** Back to the Hoverboard

Riding on a hoverboard.

.. code-block:: inform7

   Include Rideable Vehicles by Gavin Lambert.

   Park is a room. Drive is north of Park. 

   The hoverboard is a rideable vehicle in Park. The bench is an enterable supporter in Park.

   Test me with "sit on bench / stand on hoverboard / n / s / sit on bench / n".

Swearing Reloaded
=================

**Author:** Shin | **Version:** 1

Swearing as defined in Version 2/090402 of the Standard Rules by Graham Nelson.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Underside
=========

**Author:** Eric Eve | **Version:** 6.1

Allows objects to be put under other objects. An underside usually starts out
closed so that its contents are hidden from view. Requires Version 7 (or later)
of Bulk Limiter; the space under objects is limited by bulk. Underside is
compatible with Version 10 or later of Implicit Actions, but does not require
it. Version 5 of Underside avoids features deprecated in Version 6E59 of Inform.

**Basic example:** Lost Sock

Putting and Finding Objects Under Other Objects.

.. code-block:: inform7

   Include Underside by Eric Eve.

   Part 1 - Additional rule for taking

   Rule for deciding whether all includes scenery: it does not.

   Part 2 - Scenario

   The Bedroom is a room. "There's little room in here for anything but the bed, the desk and a solitary chair."

   The bed is an enterable scenery supporter in the Bedroom.

   An underside called under#bed is part of the bed.

   An odd sock is wearable. It is in under#bed.

   The player is holding a red ball.

   After dropping the red ball in the Bedroom:
      move the red ball under the bed, making it hidden;
      say "The red ball falls to the floor and rolls under the bed."

   The chair is an enterable portable supporter in the Bedroom.
   A red sock is on the chair.
   The bulk of the chair is 11.

   An underside called under#chair is part of the chair.

   The book is in under#chair.
   The scarf is in under#chair.

   The desk is a scenery supporter in the Bedroom.
   An open underside called under#desk is part of the desk.

   The pen is a thing.

   Before looking under the desk when the pen is off-stage:
     move the pen under the desk.

   Test me with "Drop ball/look under bed/put red sock under bed/look under bed/take odd sock/take ball/take red sock/look under bed/take chair/look/take all/look under desk/take all".

Variable Time Control
=====================

**Author:** Eric Eve | **Version:** 4

Allows individual actions to take a different number of seconds, or no time at
all. Also allows the standard time taken per turn to be defined as so many
seconds, which can be varied during the course of play

**Basic example:** Museum of Curiosities

Actions taking variable amounts of time.

.. code-block:: inform7

   Include Variable Time Control by Eric Eve.

   When play begins: 
      now the right hand status line is "  [turn count]/[sec-time]";
      now seconds_per_turn is 30.

   An exhibit is a kind of thing. An exhibit is usually scenery.

   Instead of taking or pushing or pulling or touching or attacking an exhibit:
     say "[no-time]The signs round the room strictly warn you to leave the exhibits alone."

   Carry out taking something: take 1 second.
   Carry out dropping something: take 1 second.
   Carry out taking inventory: take 1 second.

   The player carries a leaflet.
   The description of the leaflet is "[60 secs]The leaflet describes some of the main exhibits in the museum and explains that they were donated by Sir Robin Lightfinger."

   The Museum is a room.
   "This large hall contains a number of fascinating exhibits, which signs dotted round the room strictly tell you not to touch on pain of a £1,000 fine. The exhibits include a stuffed dodo, Codex Sinaiticus and an unexploded bomb."

   The signs are scenery in the Museum.
   The description is "[5 secs]The signs warn that the penalty for interfering with the exhibits in any way is £1,000."

   The stuffed dodo is an exhibit in the Museum.
   The description is "[2 secs]It doesn't look very lively."

   Codex Sinaiticus is a proper-named exhibit in the Museum.
   The description is "[120 secs]It's one of the oldest surviving Greek manuscripts of the entire bible, containing both Old and New Testaments. You spend some time trying to read the Greek text."

   The unexploded bomb is a proper-named exhibit in the Museum.
   The description is "It's an unexploded bomb of World War II vintage, apparently dug up from a street in the East End in 1941 and never disposed of since."

   Instead of listening to the unexploded bomb:
     say "[2 secs]It seems to be ticking."

   The bag of crisps is in the Museum.
   "A discarded bag of crisps lies on the floor."

   Understand "discarded" as the bag of crisps when the bag of crisps is not handled.

   After taking the bag of crisps for the first time: 
      say "[40 secs in all]As you pick up the bag, some of the crisps spill out onto the floor, so you have to scrabble around picking them all up."

   Test me with "take crisps/i/x leaflet/drop it/take it/take dodo/x signs/x codex/x bomb/listen to bomb/break bomb"

Verb Stripping
==============

**Author:** Nathanael Nerode | **Version:** 2.0.220521

Removes a number of verbs from the standard rules; verbs which might cause
confusion in a game whose theme is not adventure.

**Documented usage:**

.. code-block:: inform7

   2.0.220521: Version for Inform v10 (after a version number snafu)
   1/171007: Version for Inform 6M62

World Knowledge
===============

**Author:** Jeff Nyman | **Version:** 1.3

Mechanics to represent the player's knowledge and understanding about the world.

**Basic example:** Becoming Aware

Demonstrates how knowledge is gained by scope awareness of objects

.. code-block:: inform7

   Include World Knowledge by Jeff Nyman.

   The Laboratory is a room.

   A rosewood bench is a supporter in the Laboratory.

   An iron crucible is an open container on the rosewood bench.

   A cupboard is a closed openable container in the Laboratory.

   A wicker basket is an open container in the cupboard.

   A silver key is in the wicker basket.

   A Chinese puzzle box is a thing.

   The player is carrying a note.

   Instead of examining the note:
   	say "It says: 'Silver Key in Basket'.";
   	now the silver key is familiar.

   After searching the cupboard for the second time:
   	now the Chinese puzzle box is in the cupboard;
   	familiarize the Chinese puzzle box;
   	say "Digging deeper, you find a Chinese puzzle box."

   Test me with "kstate note / kstate silver key / examine note / kstate silver key / kstate bench / kstate crucible / kstate cupboard / kstate basket / open cupboard / kstate basket / examine basket / kstate basket / search cupboard / kstate Chinese puzzle box / search cupboard / kstate Chinese puzzle box".

####################################
Parser, Commands & Input
####################################

Basic Help
==========

**Author:** David Cornelson | **Version:** 1.2

**Documented usage:**

.. code-block:: inform7

   when play begins:
   	add "xyzzy" to Help Common Commands.

Before Processing a Command
===========================

**Author:** Daniel Stelzer | **Version:** 2.0.20250424

]^

**Basic example:** The Riddle of the Labyrinth

Cancelling a series of commands when something dramatic happens in the world.

.. code-block:: inform7

   say "(Since something dramatic has happened, the remainder of your command---'[player's command]'---has been cut off.)[paragraph break]";
   now the interruption flag is false;
   reject the player's command.

Command Modification
====================

**Author:** Daniel Stelzer | **Version:** 1

**Documented usage:**

.. code-block:: inform7

   force the command "jump"
   force the command set {"north", "east", "northeast"}

Command Preloading (for Glulx only)
===================================

**Author:** Daniel Stelzer | **Version:** 1.0.20230916

A simple way to preload input onto the command line before the player begins to
type.

**Documented usage:**

.. code-block:: inform7

   preload the command "take "

Compliant Characters
====================

**Author:** Nathanael Nerode | **Version:** 5.1.230727

Report parsing errors to the player when ordering other characters to do things.
Inform 7 normally redirects these errors to 'answer <topic>' so that the
character can respond to arbitrary statements. But in an story with compliant
characters who the player orders around routinely, that is frustrating to a
player who has made a typo; this helps out the player. Requires version 5 of
Neutral Standard Responses. Tested with Inform 10.1.0.

**Basic example:** Jane

Regression test

.. code-block:: inform7

   Include Neutral Standard Responses by Nathanael Nerode.
   Include Compliant Characters by Nathanael Nerode.

   Jane's house is a room. "It's Jane's house."
   Jane is a person in the house. The description of Jane is "It's Jane!"
   Persuasion rule for asking Jane to try doing something:
   	persuasion succeeds.

   The furniture is a plural-named scenery thing in the house. The description of the furniture is "The furniture is not meant to be used."
   The decorations is a plural-named scenery thing in the house. The description of the decorations is "Decorative."

   A banana is a thing.
   A red dress is a thing in the house.

   test scenery with "jane, take furniture/jane, take furniture and decorations".
   test cantsee with "jane, take banana/jane, take asdf/jane, take dress".

Excess Word Stripping
=====================

**Author:** Brent Worthington | **Version:** 2

Allows commands that are only partly understood to be reparsed after trimming
off the bits not understood.

**Basic example:** Matters of the Tart

In which the player's loquaciousness is trimmed down to the parser's level of
understanding.

.. code-block:: inform7

   Include Excess Word Stripping by Brent Worthington.

   The Kitchen is a room. "The kitchen is warm and inviting and enveloped in the smell of freshly cooked tart.".

   The oven is in the kitchen. The tart is on the oven.

   The description of the tart is "It's a small plum tart made without any sugar, so it should prove to be quite tart for a tart.".

   Test me with "take the tart with care / drop the tart savagely".

Extended Grammar
================

**Author:** Aaron Reed | **Version:** 8.2

Adds some of the most commonly attempted verb synonyms and alternate grammar
lines. Based on the Inform 6 extension ExpertGrammar.h by Emily Short.

**Basic example:** Look Around You -

.. code-block:: inform7

   Include Extended Grammar by Aaron Reed.

   The Laboratory is above the Operating Room. A slab is an enterable supporter in the Operating Room. A man called the Creature is on the slab. The player carries a raw steak. The oscillitron is a device in Operating Room. Instead of attacking the creature, say "It's alive!"

   Test me with "descend / look around / observe the creature / activate oscillitron / sit down on the slab / hand steak to Creature / place steak on slab / kick Creature / upstairs"

Glk Input Suspending (for Glulx only)
=====================================

**Author:** Gavin Lambert | **Version:** 1.1

Provides a mechanism to 'suspend' line and character inputs in progress to allow
something to be printed, and then input resumed afterwards.

**Basic example:** Compilation Check

.. code-block:: inform7

   Include Glk Input Suspending by Gavin Lambert.

   There is a room.

Numbered Disambiguation Choices
===============================

**Author:** Aaron Reed | **Version:** 10.2

Numbers the options in disambiguation questions, to help new players and solve
the 'disambiguation loop' problem caused by indistinguishable objects.

**Basic example:** Curio Shop

A setting littered with opportunities for confused input.

.. code-block:: inform7

   Include Numbered Disambiguation Choices by Aaron Reed.

   The Curio Shop is a room.

   A dog is an animal in Curio Shop. A cast iron hot dog, a hot plate, a hot iron, a dog collar, a copy of Dog Fancier magazine, and a 16mm film are in Curio Shop. A 16mm film canister is in Curio Shop.

   Test me with "x dog / 1 / x hot / x dog / 2 / x 3 / take film / 1) 16mm film".

Numbered Disambiguation Choices IT
==================================

**Author:** Leonardo Boselli | **Version:** 2

Numbers the options in disambiguation questions, to help new players and solve
the 'disambiguation loop' problem caused by indistinguishable objects.
Semplicemente tradotto in italiano.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Poor Man's Mistype
==================

**Author:** Aaron Reed | **Version:** 8

Adds basic typo correction by checking the first few letters of misunderstood
input against the printed names of nearby objects. Requires version 15 of
Smarter Parser by Aaron Reed. Supports Scope Caching by Mike Ciul for faster
performance.

**Basic example:** Potatoe Farm

.. code-block:: inform7

   Include Poor Man's Mistype by Aaron Reed.

   There is a room called On The Ol' Potato Farm. "Efforts to turn this place into a trendy retreat for artists have not been fruitful." A vegetable garden and a cemetery are fixed in place in Farm. A minuscule potato, a squash daiquiri, and an exhilarating questionnaire are in Farm. A maintenance worker named Katelynn and a committed playwright are people in Farm.

   Test me with "x potatoe / x potatos / x cemetary / tkae questionare / give potatoe to playright / hug katelyn / drop teh questionnaire / lok / drink daquiri".

Questions (for Glulx only)
==========================

**Author:** Michael Callaghan | **Version:** 5.2

An extension to allow us to suspend normal parser input to receive and respond
to answers to questions.

**Basic example:** Quiz Night

A short example to show creating a multiple choice quiz.

.. code-block:: inform7

   Include questions by Michael Callaghan.

   The pub is a room.  "The pub is crowded for the weekly quiz night.  The barman is ready to call out the questions.  Get one wrong and you will be barred from the pub for life."

   After looking for the first time:
   	follow the pub rule.

   Table of quiz questions
   Qn	Options	Correct
   "In which year was the Battle of Hastings"	{"1256", "1066", "1589", "1790"}	2
   "What type of animal is Basil Brush"	{"Cat", "Dog", "Rabbit", "Fox"}	4
   "What is the square root of 126736?"	{"356", "289", "421", "321"}	1
   "How many books are there in the Old Testament"	{"23", "39", "37", "41"}	2
   "What is a Cantaloupe?"	{"Animal", "Star", "Fruit", "Vegetable"}	3

   The expected answer is a number that varies.

   Every turn when the location is the pub (this is the pub rule):
   	choose a random row in the table of quiz questions;
   	now current question is the Qn entry;
   	now current question menu is the Options entry;
   	now expected answer is the correct entry;
   	blank out the whole row;
   	ask a closed question, in menu mode.

   A menu question rule (this is the pub answer rule):
   	if the number understood is the expected answer:
   		if the table of quiz questions is not empty:
   			say "Well done.  You have survived to the next round.";
   		otherwise:
   			end the story finally saying "Congratulations you have won!" ;
   	otherwise:
   		end the story finally saying "You have been barred from the pub for getting a question wrong." .

Reversed Persuasion Correction
==============================

**Author:** Juhana Leinonen | **Version:** 2

Automatically corrects commands given to NPCs where the order is reversed, for
example HELLO, ALICE instead of ALICE, HELLO.

**Basic example:** In the Army

A demonstration of the extension's functionality.

.. code-block:: inform7

   Include Reversed Persuasion Correction by Juhana Leinonen.

   The Training camp is a room. Private Johnson, Private Smith, Private Stevens and Private Miller are men in the training camp.

   Persuasion rule for asking people to try doing something: persuasion succeeds.

   Instead of an actor jumping:
   	say "[The person asked] jumps.";
   	rule succeeds.

   Test me with "johnson, jump/jump, johnson/private, jump/stevens/jump, private/miller".

Simple Spelling
===============

**Author:** Alice Grove | **Version:** 2.2

Simple Spelling aims to make stories more screen-reader-friendly by allowing
players to request the spelling of any visible thing. This extension adds two
actions: 'listing visible items for spelling' and 'spelling the numbered word.'

**Basic example:** Simple Spelling Lab

A room with some spellable items and characters.

.. code-block:: inform7

   Include Simple Spelling by Alice Grove.


   A dictionary is a kind of thing.

   Spelling Lab is a room.

   Donna Hopkins-Brown is a woman in Spelling Lab. Donna Hopkins-Brown carries 4 dictionaries.

   An inspection table is a supporter in Spelling Lab. A perse purse is on the inspection table. A pale pail is on the inspection table. A piece of Pete's pizza is on the inspection table.

   The player carries a xyzzifier.


   Test me with "spell / spell 1 / spell 2 / spell 3 / spell 4 / spell 5 / spell 6 / spell 7 / spell 8".

Smarter Parser
==============

**Author:** Aaron Reed | **Version:** 16.1

Understands a broader range of input than the standard parser, and can direct
new players towards proper syntax.

**Basic example:** Caverns and Kobolds

A tiny scenario to test misunderstood input with.

.. code-block:: inform7

   Include Smarter Parser by Aaron Reed.

   Spooky Cave is a room. A glowing sword is in Spooky Cave. Dark Tunnel is north of Spooky Cave. A dusty skull is in Dark Tunnel. The kobold is a man in Tunnel. The kobold holds a spear.

   A smarter parser rule (this is the no leet speak allowed rule):
   	if input contains "\w\d+\w":
   		identify error as no leet speak allowed rule;
   		reject the command.

   A smarter parser rule (this is the stripping formal address rule):
   	if stripping "(sir|maam)" is fruitful:
   		identify error as stripping formal address rule;
   		reparse the command.
   		
   A smarter parser rule (this is the signs of frustration rule):
   	if input contains "(stupid|damn|idiot|hate)":
   		identify error as signs of frustration rule;
   		reject the command.

   The stripping formal address rule is listed first in the smarter parser rules.

   Table of Smarter Parser Messages (continued)
   rule name			message
   no leet speak allowed rule		"This story requires you to use proper spelling and grammar."
   stripping formal address rule		"Oh please, we don't stand on titles here."
   signs of frustration rule		"If you're feeling frustrated, you can always SAVE and come back later."

   Test me with "ub4r l33t / novice off / who am i? / novice on / who am i??? / sword / i'll look at the sword / which way should I go / what do I do then?? / i'm so confused / walk over to the sword / try looking / please take the sword sir / drop the freaking sword / the hell / who are you / look around the area / I want to take the sword / why is the sky blue / go somewhere / carefully go north / anyway look around / you're very tall / hello / get kobold's spear / touch ceiling / touch skull with my foot / wait for a while / well it looks like i'm starting to figure it out".

Subcommands
===========

**Author:** Daniel Stelzer | **Version:** 2.0.221104

Exposes the snippets referring to each noun.

**Basic example:** Subcommand Laboratory

A simple demonstration of how subcommands affect the parser.

.. code-block:: inform7

   say "Verb subcommand: [the subcommand of the verb].";
   if the noun is not nothing:
   	say "Noun subcommand: [the subcommand of the noun].";
   if the second noun is not nothing:
   	say "Second noun subcommand: [the subcommand of the second noun].";
   continue the action.

####################################
Release, Metadata & Licensing
####################################

Configurable Creative Commons License
=====================================

**Author:** Creative Commons | **Version:** 1.2

Allows easy implementation of a Creative Commons Public License of the author's
choice.

**Documented usage:**

.. code-block:: inform7

   http://creativecommons.org/about/licenses/meet-the-licenses

Creative Commons Public License IT
==================================

**Author:** Leonardo Boselli | **Version:** 2

Un'estensione in italiano per facilitare il rilascio di 'interactive fiction'
secondo la Creative Commons License v25. Basata sull'estensione GNU General
Public License v3 di Otis T. Dog.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Spanish Language
================

**Author:** Sebastian Arg | **Version:** 2.0.0

To make Spanish the language of play. Release 230724

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

########################################
Rules, Relations & Programming Utilities
########################################

Achievements
============

**Author:** Juhana Leinonen | **Version:** 1.2

A simple but flexible rule-based achievement system. Awarded achievements can
optionally persist in external files after a restart.

**Basic example:** Another Day at the Office

Rule-based and manually awarded achievements

.. code-block:: inform7

   Include Achievements by Juhana Leinonen.

   Office is a room. "It's another boring afternoon in the office."

   The desk is in the office. The inbox is on the desk. The memo is in the inbox.

   A piece of gum is a thing.

   The time of day is 4:57 PM.

   Instead of looking under the desk for the first time:
   	say "Hey, someone stuck a piece of gum under the desk!";
   	now the player is carrying the piece of gum.
   	
   After examining the memo:
   	say "It's from the boss. You forget it as soon as you've read it.";
   	award the "Diligent Employee" achievement.
   	
   Table of Achievements
   achievement	description	validation	awarded
   "Desk Treasure"	"You found the piece of gum."	gum achievement rule	false
   "Diligent Employee"	"You read the memo."	--	false
   "Overtime"	"Stayed at work past 5 pm."	overtime achievement rule

   This is the gum achievement rule:
   	if the player is carrying the piece of gum:
   		rule succeeds.
   		
   This is the overtime achievement rule:
   	if the time of day is greater than 5:00 PM:
   		rule succeeds.

   Instead of exiting:
   	say "Ok, that's enough for today.";
   	end the story finally.
   	
   Test me with "read memo/look under desk/z/z/exit".

Actions on Groups
=================

**Author:** Matt Weiner | **Version:** 1

Allows us to make certain actions apply to an entire player-specified group all
at once, rather than applying serially to each member of the group.

**Basic example:** Sword Talk

Allowing a response to "ask smith about swords" while blocking any other attempt
to ask about multiple things.

.. code-block:: inform7

   Include Actions on Groups by Matt Weiner.

   Section 1 - Swords and the Ideal Sword

   A sword is a kind of thing.

   Understand "blade/edge/sword" as "[blade]".
   Understand "[blade]" as sword.

   Definition: a thing is perfect if it is nowhere.

   The ideal sword is a sword.
   Understand "blades/edges" as the ideal sword.

   Section 2 - Quizzing

   Understand the command "ask" as something new. 

   Quizzing it about is an action applying to one thing and one visible thing.
   Understand "ask [someone] about [things]" as quizzing it about.

   Does the player mean quizzing about a perfect thing: it is very likely.

   To decide what action name is the action-to-be: (- action_to_be -).
   After deciding the scope of the player when the action-to-be is the quizzing it about action:
   	repeat with item running through things:
   		place item in scope.

   Section 3 - Setting Action on Groups for Quizzing

   Quizzing is groupable action.
   Quizzing is group-only action. 

   Action on groups for quizzing when dealing with the list of swords:
   	clear the multiple object list;
   	try quizzing the noun about the ideal sword.
   	
   The can't use undesignated groups rule response (A) is "'Sorry, one question at a time!'"

   Section 4 - Scenario

   The swordsmith is a man. "The swordsmith wears a button that reads 'ASK me ABOUT swords, or about a particular sword!'" Understand "smith" as the swordsmith. The swordsmith wears a button. The description of the button is "'ASK me ABOUT swords, or about a particular sword!'"

   The rakish fop is a man. The fop holds a sword called the wicked needle.
   The dolorous monk is a man. The monk carries a sword called the keen instrument of DEATH.

   After quizzing the swordsmith about the ideal sword, say "'Yes, swords are the best!'"
   After quizzing the swordsmith about a sword (called blade), say "'Hmm, [the blade]... not my best work, to be honest.'"

   The forge is a room. All men are here. The player is the monk.

   Test me with "ask smith about sword/ask smith about my sword/ask smith about swords/ask smith about needle and instrument".

Adaptive Hints
==============

**Author:** Eric Eve | **Version:** 7

An adaptive hint system based on Menus by Emily Short.

**Basic example:** Escape from an Old House

A short game with several adaptive hints

.. code-block:: inform7

   Include Adaptive Hints by Eric Eve.
   Use scoring.

   Part 1 - Hint Tables

   Table of Potential Hints (continued)
   title	subtable	
   "What should I do now?"	Table of General Hints	
   "What can I do in the Hall?"	Table of Hall Hints
   "What should I do in the Lounge?"	Table of Lounge Hints	
   "How do I open the front door?"	Table of Front Door Hints
   "How do I unlock the tall cabinet?"	Table of Cabinet Hints
   "How can I get through the window?"	Table of Window Hints
   "How do I unlock the front door?"	Table of Iron Key Hints

   Table of General Hints
   hint	used
   "Try exploring a bit."	a number
   "Then trying exploring a bit more."
   "Have you explored enough yet?"

   Table of Lounge Hints
   hint	used
   "Look around."
   "But frankly there's not much here."
   "Except that mouldy old carpet."

   Table of Hall Hints
   hint	used
   "Search it thoroughly."
   "What did you find?"
   "Perhaps that tall cabinet is worth investigating."

   Table of Cabinet Hints
   hint	used
   "Obviously, you need to find a key."
   "Maybe it's been dropped somewhere."
   "Somewhere not that obvious."
   "And maybe it slid under something."
   "Like a carpet."

   Table of Front Door Hints
   hint	used
   "Well, finding the key would be a start."
   "It may not be far from the front door"
   "Have you tried looking in the cabinet?"
   "What did you find there?"

   Table of Iron Key Hints
   hint	used
   "What did you find in the hall cabinet?"
   "How thoroughly have you examined it?"
   "Did it have a pocket?"
   "What was in the pocket?"


   Table of Window Hints

After Not Doing Something
=========================

**Author:** Ron Newcomb | **Version:** 2.1

Allows us to write rules that happen after an action fails, such as 'After not
examining or searching something'. 'After Not Doing Something' is short for
'After Failing To Do Something'

**Basic example:** I Try, and I Try

Some people are never happy.

.. code-block:: inform7

   Include after not doing something by Ron Newcomb.

   Your parent's house is a room. Your disapproving mother is a woman, here. A TV is fixed in place, here.

   After not doing something, say "In the background, you hear your mother sigh.  'Oh if you'd only worked harder, [the current action] wouldn't be a problem now, would it?'"

   After not pushing or rubbing something, say "Your mother sighs.  'Here, *I'll* get it for you.'"

   Test me with "go outside / turn on TV / dust TV / push TV / nap".

Atmospheric Effects
===================

**Author:** Mikael Segercrantz | **Version:** 6.2

A table-based way to add atmospheric effects to rooms, regions, things and
scenes.

**Basic example:** Forest and Clearing

A simple example of regional and room effects, and ignoring messages.

.. code-block:: inform7

   Include Version 6 of Atmospheric Effects by Mikael Segercrantz.

   Western Edge of the Forest is a room. East of the western edge of the forest is a room called A Forest Clearing. East of a forest clearing is a room called Eastern Edge of the Forest.

   The Forest Region is a region. Western edge of the forest, a forest clearing and eastern edge of the forest are in the forest region.

   Table of Atmospheric Definition (continued)
   loci			ignoring		subtable
   A Forest Clearing		ignore		Table of Clearing Definition
   Forest Region		do not ignore	Table of Forest Definition

   Table of Clearing Definition
   during		initch	latch		aftcnt		curcnt		sctype		runtype		frtype		igtype		subtable
   a scene		50	a number	a number	a number	fully random	a running type	a further type	an ignoring type	Table of Clearing Atmosphere

   Table of Clearing Atmosphere
   used		message
   a number	"The sound of a small river running nearby reaches your ear."
   --		"A cuckoo can be heard not far away." 

   Table of Forest Definition
   during		initch	latch	aftcnt	curcnt		sctype	runtype		frtype		igtype		subtable
   a scene		75	33	5	a number	random	a running type	a further type	an ignoring type	Table of Forest Region Atmosphere

   Table of Forest Region Atmosphere
   used		message
   a number	"A fox runs across the path."
   --		"Birds chirp off in the distance."
   --		"A rabbit bounces off with sudden haste."

Character Portraits
===================

**Author:** Nathanael Nerode | **Version:** 1.0.220523

Provides a complex system for customzing the printed descriptions of characters
wearing or carrying lots of stuff, similar to the room description system in
Standard Rules. Requires Large Game Speedup by Nathanael Nerode.

**Documented usage:**

.. code-block:: inform7

   set the portrait priority of (object) to 5

Commonly Unimplemented
======================

**Author:** Aaron Reed | **Version:** 2

Responds to attempts to interact with unimplemented clothing, body parts, or
generic surroundings. Requires Smarter Parser by Aaron Reed.

**Basic example:** Noses

Subtitle of this example.

.. code-block:: inform7

   Include Smarter Parser by Aaron Reed.
   Include Commonly Unimplemented by Aaron Reed.

   Stage is a room. Bob and Phil are people in Stage.
   A nose is a kind of thing. A nose is part of every person.

   Nose poking is an action applying to one thing. Understand "poke [something]" as nose poking. Check nose poking: if noun is not a nose, instead say "Only for noses!". Carry out nose poking: say "Strangely satisfying."

   When play begins: release body part word "nose" from Smarter Parser.

   Table of Smarter Parser Messages (continued)
   rule name	message
   flexible stripping body parts rule	"[as the parser]You do not normally need to refer to parts of the body; except in the case of noses, which you can try to POKE.[as normal]"

   test me with "x phil's nose / pick phil's nose / punch phil in the nose / poke phil's cheek / poke my nose"

Conversation Suggestions
========================

**Author:** Eric Eve | **Version:** 6.2

Provides a means of suggesting topics of conversation to the player, either in
response to a TOPICS command or when NPCs are greeted. This extension requires
Conversation Framework. Version 3 makes use of Complex Listing by Emily Short if
it's included in the same game rather than indexed text to generate a list of
suggestions.

**Basic example:** The Lion in Winter

Suggestions for a conversation fit for a king.

.. code-block:: inform7

   Part 1 - Setup and Topics

   Include Conversation Suggestions by Eric Eve.

   Richard is a familiar man.

   Eleanor of Aquitaine is a familiar woman.
   Understand "queen" as Eleanor.

   Bertrand de Born is a man.

   Thomas Becket is a familiar man.

   Alice of Berangaria is a woman.

   England is a familiar thing.
   France is a familiar thing.
   Prince John is a familiar man.
   doggerel is a familiar thing.

   The player carries a sword. 
   Understand "weapon" or "your" as the sword.

   sword-suggestion is a misc-suggestion. The printed name is "show him your sword".

   Part 2 - The King

   The Solar is a Room. "Dimly lit by the pale winter sun, the Solar overlooks the snow-covered bailey."

   King Henry is a man in the Solar. "King Henry is pacing up and down the Solar like a caged lion."
   The description is "He looks full of energy, as if anxious to get on with building the Angevin Empire instead of being cooped up in a wintry castle."

   The ask-suggestions are { France, Alice, Richard,  Eleanor,  Bertrand,  Thomas  }.
   The tell-suggestions are { England, Prince John }.
   The other-suggestions are { sword-suggestion }.

   Understand "plantagenet" or "II" or "the second" as King Henry.

   Part 3 - Conversation

   After quizzing King Henry about France:
    say "'[remove france ask suggestion]'I rule more of it than the King of France does!' he boasts."

   After quizzing King Henry about Thomas:
     say "[remove thomas ask suggestion]'Don't talk to me about that meddlesome priest!' the king growls."

   After quizzing King Henry about Eleanor:
     say "[make bertrand known][remove eleanor ask suggestion]'She'll be joining me here shortly, and I'm looking forward to it. But I do wish that scoundrel Bertrand de Born would stop singing songs about her!' the king exclaims."

   After quizzing King Henry about Bertrand:
     say "[remove bertrand ask suggestion][add doggerel ask suggestion]'That wretched minstrel stirs up more trouble with his doggerel than a score of knights with their swords!' the king complains."

   After quizzing King Henry about doggerel:
   say "[remove doggerel ask suggestion]''Bertrand's latest ditty goes something like this,' scowls the king: 'Alas poor prisoner, poor prisoner return, to thy people, Eleanor, who weep and mourn;  my tears are my bread both night and day, alas how long is my exile!'"

   After quizzing King Henry about Richard:
    say "[remove richard ask suggestion][make alice known]'I just don't know: he's a good enough warrior, but I do wish he'd marry, I sometimes worry about him. Alice is comely enough, after all!' the king remarks."

   After quizzing King Henry about Alice:
    say "[remove alice ask suggestion]'Well, Richard should have shown more interest in her. If he wouldn't take her himself he's only himself to blame if I decorate his head with antlers!' Henry yells."

   After informing King Henry about England:
    say "[remove England tell suggestion]'I'm sure England can manage without me until the spring,' Henry replies."

   After informing King Henry about Prince John:
    say "[remove Prince John tell suggestion]'I'm glad to hear John will be here soon. He's the only one who's really loyal to me, you know!' King Henry declares."

   Instead of showing the sword to King Henry:
    say "[remove sword-suggestion other suggestion]'That's a fine weapon you have there,' the king approves."

   Part 4 - Testing

   test me with "talk to the king/a thomas/t england/topics/a france/t john/topics/a richard/a eleanor/topics/a alice/a bertrand/topics/a doggerel/show sword/topics"

Dynamic Tables
==============

**Author:** Tara McGrew | **Version:** 5.1.0

Provides a way to change the capacity of a table during the game.

**Basic example:** Notlob

A parrot that assigns a value to everything he hears, and repeats the lines back
in his preferred order.

.. code-block:: inform7

   Include Dynamic Tables by Tara McGrew.

   Pet Shoppe is a room. "A sign reads: 'If you're looking for pets, look no further! Pets are something we sell and you can buy them from us.'"

   The parrot is an animal in the Pet Shoppe. "A parrot is perched here." Instead of buying the parrot, say "Except that one."

   Table of Parrot Quips
   quip text	quip score	usage count
   indexed text	a number	a number

   The highest quip score is a number that varies. The highest quip score is 0.

   After answering the parrot that:
   	let the textual quip be indexed text;
   	let the textual quip be the topic understood;
   	let the current quip score be the calculated quip score of the textual quip;
   	if the number of blank rows in the Table of Parrot Quips is 0, change the Table of Parrot Quips to have (2 * the number of rows in the Table of Parrot Quips) rows;
   	choose a blank row in the Table of Parrot Quips;
   	now the quip text entry is the textual quip;
   	now the quip score entry is the current quip score;
   	now the usage count entry is 0;
   	sort the Table of Parrot Quips in reverse quip score order;
   	if the current quip score is greater than the highest quip score:
   		say "The parrot listens intently, whistling with excitement.";
   		now the highest quip score is the current quip score;
   	otherwise:
   		say "The parrot listens."

   To decide which number is the calculated quip score of (msg - indexed text):
   	let msg be msg in lower case;
   	let the result be 0;
   	repeat with N running from 1 to the number of characters in msg:
   		let C be character number N in msg;
   		if C is "p" or C is "a" or C is "r" or C is "o" or C is "t", increase the result by 1;
   	decide on the result.

   Every turn when the highest quip score is greater than 0:
   	choose row 1 in the Table of Parrot Quips;
   	say "The parrot squawks, '[quip text entry]'";
   	increase the usage count entry by 1;
   	if the usage count entry is 3:
   		blank out the whole row;
   		if the number of filled rows in the Table of Parrot Quips is 0:
   			now the highest quip score is 0;
   		otherwise:
   			sort the Table of Parrot Quips in reverse quip score order;
   			choose row 1 in the Table of Parrot Quips;
   			now the highest quip score is the quip score entry.

   Test me with "say hello polly / say hello polly parrot / say i've got a lovely fresh cuttlefish for you / say pining for the fjords / z / z / z / z".

Exit Lister
===========

**Author:** Eric Eve | **Version:** 11

A status line exit-lister and an EXITS command, with optional colouring of
unvisited exits. Selected rooms and doors can be optionally be excluded from the
list of exits.

**Basic example:** Exploring the Dark

Hiding and Showing Dark Exits

.. code-block:: inform7

   Include Exit Lister by Eric Eve.

   The Secluded Grove is a room. "You stand just outside the mouth of a dark cave to the east."

   The blazing torch is in the Secluded Grove. It is lit.

   The Dark Cave is east of Secluded Grove. 
   "The main exit is to the east. Other exits lead north and south."
   It is dark.

   Narrow Crawl is north of Dark Cave. "This seems to be a dead end. The only way out is back south." It is dark.

   Long Tunnel is south of Dark Cave. "The tunnel comes to a dead end. The only way out is back north." It is dark. 

   Instead of thinking:
   	say "You have a [if dark-exits-invisible is true]bright[otherwise]dim[end if] idea, as a result of which you [if dark-exits-invisible is true]can[otherwise]can't[end if] now see darkened exits.";
   	now dark-exits-invisible is whether or not dark-exits-invisible is false.
   	
   Instead of going nowhere when in darkness: say can't see way in dark.

   Instead of going to a darkness-occluded room: say can't see way in dark.

   To say can't see way in dark: say "It's too dark to see where you're going."

Extended Debugging
==================

**Author:** Erik Temple | **Version:** 2.2

Provides a way for the author to release a build of a game while retaining both
custom and built-in debugging commands. Also wraps Inform's debug tracing
routines in phrases that authors can use to trigger rule-tracing from the source
text rather than from the command prompt and provides other debugging features.

**Documented usage:**

.. code-block:: inform7

   Section - Debugging Control

Far away
========

**Author:** Jon Ingold | **Version:** 5.2

Creates an adjective for far-off items which cannot be touched.

**Basic example:** Christmas Morning

A simple example of distance, and how to overcome it.

.. code-block:: inform7

   Include Far Away by Jon Ingold.

Footnotes
=========

**Author:** Stephen Granade | **Version:** 2

Provides a framework for organizing and displaying footnotes in a game. Version
2 makes Footnotes responsive and 6L38-compatible.

**Basic example:** Shameless Plug

Adds a footnote to the description of one object in the game.

.. code-block:: inform7

   Include Footnotes by Stephen Granade. Footnotes are on.

   The Lab is a room. "Filled with all of the equipment that you need to trap neutral lithium atoms and cool them to just above absolute zero."

   The carbon dioxide laser is in the Lab. "On one side of the lab is a carbon dioxide laser." The description is "It utilizes a flowing gas approach rather than a closed tube and is specially designed to be extremely stable[note laser-ref]." It is fixed in place. Understand "co2" as the laser.

   Table of Footnotes (continued)
   Name	Note	
   laser-ref	"K. M. O’Hara, S. R. Granade, M. E. Gehm, T. A. Savard, S. Bali, C. Freed, and J.E. Thomas, Ultrastable CO2 laser trapping of lithium fermions, Phys. Rev. Lett., vol. 82 (1999), pp. 4204."

   Test me with "x laser / note 1".

Gender Options
==============

**Author:** Nathanael Nerode | **Version:** 4.0.220604

More broad-minded English language gender/number model where male, female, and
neuter are three separate true-false properties. Allows for objects to respond
to any specified combination of HE, SHE, IT, and THEY. As fast as the Standard
Rules. Tested with Inform v10.1.0.

**Basic example:** It for All

Some authors have requested that "it" apply to anything, plural or singular, of
any gender, for the convenience of their players.

.. code-block:: inform7

   Include Gender Options by Nathanael Nerode.

   A person is neuter. A man is neuter.  A woman is neuter.  [Overrides "usually not neuter", makes people respond to IT]
   A plural-named thing is ambiguously plural. [Makes all plural-named objects respond to IT]
   Prefer neuter gender is false. [Printed text shouldn't refer to characters as "it" if they're male or female.]

   Marching Grounds is a room.  "The place for marching!"

   to march is a verb. to watch is a verb.

   The soldiers are plural-named men in Marching Grounds. 
   The description of the soldiers is "[Regarding the soldiers][They] [march] up and down."

   An observer is a improper-named woman in Marching Grounds.
   The description of the observer is "[Regarding the observer][They] [watch] the soldiers."

   test pronouns with "x soldiers / pronouns / x observer / pronouns".

Hypothetical Questions (for Glulx only)
=======================================

**Author:** Tara McGrew | **Version:** 5.1.0

Allows us to test the consequences of a phrase or action without permanently
changing the game state.

**Basic example:** A Sense of Adventure

Letting the player know what will happen if he picks up nearby objects.

.. code-block:: inform7

   Include Hypothetical Questions by Tara McGrew.

   Use scoring.

   The maximum score is 5.

   Hallway is a room. "This hall leads east and west. There's also a door to the south."

   Trophy Room is east of the hallway. "This room is absolutely jam-packed with trophies. The exit is to the west."

   A golden idol is in the trophy room. After taking the golden idol for the first time, increase score by 5.

   Danger Zone is west of the hallway. "This room is full of various hazards. If you know what's good for you, you'll leave to the east."

   A cursed idol is in the danger zone. After taking the cursed idol: say "As you pick up the idol, you feel an evil presence sucking the life force out of your body."; end the story.

   Winners' Lounge is south of the hallway. "This is where winners hang out. A door to the north leads back to the hallway."

   The Mask of Victory is here. "A strange mask is hanging on the wall here. A sign beneath it simply states: 'The Mask of Victory'." After taking the Mask of Victory, end the story finally.

   Report going:
   	hypothetically take everything and consider the player's fate rulebook;
   	if the outcome of the rulebook is:
   		-- the player dies outcome: say "You sense an ominous presence. Better be careful picking things up in here!";
   		-- the player wins outcome: say "You sense your victory is at hand!";
   		-- the player scores outcome: say "You sense a potential profit. Better grab everything you can!".

   To take everything:
   	repeat with X running through things in the location:
   		try taking X.

   Player's fate is a rulebook. The player's fate rulebook has outcomes player dies, player wins, player scores, and nothing noteworthy (success - the default).

   A player's fate rule when the story has ended finally: player wins.

   A player's fate rule when the story has ended: player dies.

   A player's fate rule when the score is greater than the last notified score: player scores.

   Test me with "w / e / e / get idol / w / s / get mask".

In-Line Topical Hints
=====================

**Author:** Andrew Schultz | **Version:** 2.3

Lets the author offer the player in-line hints, with options for presentation.
This extension requires Inform 6M62 or higher to run.

**Basic example:** Fetch Quest

A minimal game with hints, rule-dependent and not

.. code-block:: inform7

   the story headline is "a minimal example".

   there is no score in this story.

   the print final score rule is not listed in any rulebook.

   include In-Line Topical Hints by Andrew Schultz.

   the bronze coin is a thing.
   the silver coin is a thing.
   the gold coin is a thing.

   the description of a room is usually "[if number of viable directions is 1]The only exit leads[else]Exits lead[end if] [list of viable directions]."

   definition: a direction (called di) is viable:
   	if the room di of the location of the player is nothing, decide no;
   	decide yes;

   description of the player is "As good-looking as ever, but someone or something wrote something on you: N.GET ALL.S.E.GET ALL.W.W.GET ALL.E.S.".

   check dropping:
   	say "No way! The coin is too valuable, or something." instead;

   Center Room is a room. "You can go north to the bronze room, east to the silver room, west to the gold room, or south to the glass room."

   Bronze Room is north of Center Room.

   check going nowhere:
   	say "[if player is in center room]You can go any of the four directions[else]Only one way out[end if]."

   Silver Room is east of Center Room. "You can go back west."

   Gold Room is west of Center Room. "You can go back east."

   Glass Room is south of Center Room. "You can go back north."

   The bronze coin is in Bronze Room.

   when play begins:
   	now hint-crit-only is true;
   	activate bronzy;

   after taking the bronze coin:
   	now the silver coin is in Silver Room;
   	activate silvery; [you can deactivate bronzy here if you want, but I deliberately avoided this to show topic disambiguation]
   	continue the action;
   	
   after taking the silver coin:
   	now the gold coin is in Gold Room;
   	activate goldy; [you can deactivate silvery here if you want, but I deliberately avoided this to show topic disambiguation]
   	continue the action;

   after going to Glass Room:
   	if player has gold coin:
   		end the story saying "YOU GOT ALL THE LOOT, AND YOU ESCAPED!";
   	continue the action;

   bronzy is a hint-topic. printed name is "Finding the bronze coin".

   hint-list of bronzy is table of bronzy hints.

   table of bronzy hints
   hint-text	done-yet	show-rule
   "The bronze coin is not in the Center Room."	false	a rule
   "It's in the bronze room."
   "North of the Center Room."

   silvery is a hint-topic. printed name is "Finding the silver coin".

   hint-list of silvery is table of silvery hints.

   table of silvery hints
   hint-text	done-yet	show-rule
   "The silver coin is somewhere in the maze."	false	a rule
   "It's in the silver room."
   "The silver room is east of the Center Room."

   goldy is a hint-topic. printed name is "Finding the gold coin.".

   hint-list of goldy is table of goldy hints.

   table of goldy hints
   hint-text	done-yet	show-rule
   "The gold coin is somewhere in the maze."	false	a rule
   "It's in the Gold Room."
   "Gold Room is west of the Center Room."
   "Once you get the gold coin, you can get out of the maze back at the Glass Room, south of the Center Room."

   get-out is a rule-dependent hint-topic. printed name is "Getting out.".

   hint-list of get-out is table of get-out hints.

   table of get-out hints
   hint-text	done-yet	show-rule
   "There's one room left where nothing's turned up. Well, other than the center."	false	a rule
   "Go south from the center."

   avail-rule of get-out is the can-win rule.

   this is the can-win rule:
   	if the player has the gold coin, the rule succeeds;
   	the rule fails.

   is-this-easy is a noncritical active hint-topic.  hint-list is table of is-easy hints. printed name is "Isn't this example too easy for a real game?"

   table of is-easy hints
   hint-text	done-yet	show-rule
   "Yes, it is, but I was going for practicality."	false	a rule
   "It didn't make sense to get too fancy."
   "However, having good test cases is important, so here I'm making a semi-long hint topic to test that."
   "There is nothing of value from here on out."
   "I basically want a topic where I can test various behaviors in a long table, so I am sure nothing in my extension is broken."
   "One more random hint should do it."
   "There we go."

   volume testing - not for release

   test win with "n/get all/s/e/get all/w/w/get all/e/s"

   test hprod with "hintdebug/n/get all/hint/topic 1/x me/topic 1"

   test hintchange with "n/get all/s/hint/n/topic 1/topic 2"

   test block with "hint block/hint/hint all/h/t/topic/topic 1/t 1/t1/1/hint block/hint all/hint review/hint one/hint recent/hint on/hint off/"

   [end example]

List Control
============

**Author:** Eric Eve | **Version:** 4

Provides a means of using tables as shuffled, cyclic or stop lists.

**Basic example:** Family Reunion

Using Tables to give successions of responses to questions and NPC fidgets

.. code-block:: inform7

   Part 1 - Setup

   Include List Control by Eric Eve.

   The description of yourself is "Trim and upright, with a proud Prussian bearing - too bad about the withered arm, though."


   Part 2 - Scenario

   The Royal Lounge is a room. "Opulent in its way, to your eye this room nevertheless has a slightly dingy, old-fashioned look, no doubt because the Queen is so opposed to the idea of change, but also perhaps because England is so backward-looking compared with your new dynamic Germany."

   The window is scenery in the lounge. "It affords an excellent view of Windsor Great Park - or rather it would if the view were not largely obscured by the Prince of Wales."

   Bertie is a man in the Lounge. "Bertie is standing with his back to the window."
   Understand "prince" or "edward" or "of" or "wales" or "uncle" as Bertie.

   Queen Victoria is a woman in the Lounge. "Queen Victoria is sitting glowering sternly at her oldest son." The description is "She's still dressed in the black mourning weeds she's worn ever since the Prince Consort died."


   Part 3 - Queen Victoria's Conversation

   Instead of asking Queen Victoria about a topic listed in the Table of Queen Conversation:
   	if there is a List Table entry, show the next response from the List Table entry;
   	otherwise say "[Response entry][paragraph break]".

   After asking Queen Victoria about something:
    	show the next response from the Table of Queen's Default Responses;
    	stop the action.

   Understand "bertie" or "uncle" or "prince" as "[prince]".

   Table of Queen Conversation
   Topic		List Table				Response
   "[prince]"	Table of Queen's Bertie Responses		--
   "germany"	Table of Queen's Germany Responses	--
   "weather"	--					"'What do you think of the weather today, grandma?' you ask.[paragraph break]'It is tolerable,' she replies."


   Table of Queen's Bertie Responses
   response
   "'Isn't Uncle Bertie looking well?' you gush.

   'He's put on too much weight,' the Queen demurs critically."
   "'Are you keeping Bertie busy, grandma?' you enquire.

   'Bertie spends far too much time gallivanting,' the Queen disapproves."
   "'Don't you think Bertie will make a fine king one day, grandma?' you ask.

   'Over my dead body!' she replies fiercely."
   "Perhaps you have exhausted that topic for now."

   Table of Queen's Germany Responses
   response
   "'You should come and visit us in Germany, grandma,' you suggest.

   'Yes, I am sure Vicky would be pleased to see me,' she nods."
   "'Our two countries should become better friends, don't you think, grandma?' you propose.

   'That was always my dear Albert's dearest wish,' she smiles."
   "'Between us, Britain and Germany could rule the world!' you declare enthusiastically, 'What do you say, grandma?'

   'Well!' she frowns, looking slightly alarmed."
   "Bertie frowns and motions to you to keep quiet."


   Table of Queen's Default Responses
   response
   "'We are not amused, Willi,' she replies sternly."
   "'That is not something we are prepared to discuss,' she answers stiffly."
   "'I am surprised you should raise such a matter at such a time!' she rebukes you."
   "'No, we shall not discuss that!' she rules."


   Table of Table Types (continued)
   tabname				index	tabtype
   Table of Queen's Bertie Responses		0	stop-list
   Table of Queen's Germany Responses	0	stop-list
   Table of Queen's Default Responses	0	shuffled-list


   Part 4 - Bertie's Fidgeting

   Table of Bertie's Fidgets
   response
   "Uncle Bertie clears his throat."
   "Uncle Bertie shuffles from one foot to the other."
   "The Prince of Wales manfully stifles a yawn."
   "Bertie scratches his right ear."
   "Bertie pats his jacket as if looking for a cigar, but then remembers himself just in time."

   Table of Table Types (continued)
   tabname				index	tabtype
   Table of Bertie's Fidgets			0	cyclic-list

   Every turn when a random chance of 1 in 3 succeeds:
   	  show the next response from the Table of Bertie's Fidgets.

   Part 5 - Test

   Test me with "x bertie/x queen/x window/ask queen about bertie/g/g/g/ask queen about weather/ask queen about love/ask queen about war/ask queen about germany/g/g/g/ask queen about William Gladstone/ask queen about Disraeli/ask queen about germany"

List Controller
===============

**Author:** Eric Eve | **Version:** 4

Provides a means of using tables as shuffled, cyclic or stoping lists. This is
an alternative to List Control that uses list controller objects instead of a
Table of Table Types.

**Basic example:** Magic Jumping

Mixing Events and responses in a list controller table

.. code-block:: inform7

   Include List Controller by Eric Eve.

   The Magic Chamber is a Room.
     "The chamber is quite bare, but you've heard it pays to jump here. "

   Instead of Jumping:

Phrases for Tables with Topics
==============================

**Author:** Ron Newcomb | **Version:** 3

This grants five new phrases regarding the player's command, the matched text,
and the topic understood: if one is a topic listed in a table, if one includes
or matches a topic listed in a table, what corresponds to one within a table,
and the last phrase corrects a bug so the topic understood may be used within an
understand-as-mistake line.

**Basic example:** Fear and Surprise

A brief demonstration of power.

.. code-block:: inform7

   Include Phrases for Tables with Topics by Ron Newcomb.

   The cathedral is a room.  There is a woman called witch. The player is a witch. 

   The Spanish Inquisition is a scene. "'All witches know magic words!  Tell us, witch, what they are!'"
   The Spanish Inquisition begins when play begins.
   The Spanish Inquisition ends when the player's command includes a topic listed in the table of magic words.
   When the Spanish Inquisition ends, say the response corresponding to a topic of the player's command from the table of magic words.

   Table of magic words
   topic		response
   "xyzzy"	"Suddenly you pop out of existence!"
   "plugh"	"In a swirl of feathers, you disappear!"

   Understand "[text]" as a mistake ("'[fix topic understood]We know that [topic understood] is not a magic word! You cannot fool us, witch!'") when the Spanish Inquisition is happening and the player's command is not a topic listed in the table of magic words.

   After reading a command when the player's command matches a topic listed in the table of magic words:
   	follow the scene changing rules;
   	replace the player's command with "x me";
   	move the player to the forest.

   The forest is a room.

   Test me with "no / foo / plugh / foo".

Points Awarding Reloaded
========================

**Author:** Shin | **Version:** 1

Points Awarding as defined in Version 2/090402 of the Standard Rules by Graham
Nelson.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Possible Movements
==================

**Author:** Peter Orme | **Version:** 2.2

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Prepositional Correctness
=========================

**Author:** Gavin Lambert | **Version:** 2.3.1

Provides a way to customise the prepositions used to refer to containment or
support, and perhaps other custom relationships added by other extensions.

**Basic example:** Horseback

Riding a horse with Rideable Vehicles.

.. code-block:: inform7

   Include Rideable Vehicles by Graham Nelson.
   Include Prepositional Correctness by Gavin Lambert.

   Grasslands is a room.  "Wide open grasslands stretch as far as the eye can see."

   A horse is a kind of rideable animal.  Understand "horse" as a horse.

   Spirit is a horse in Grasslands.  "Spirit grazes aimlessly nearby."
   The description is "This is your horse, of course, of course."

   Test me with "mount horse / l".

Reactable Quips
===============

**Author:** Michael Martin | **Version:** 10.1

A table-based approach to NPC conversation chains, as well as allowing rules to
fire on lines of conversation.

**Basic example:** Think Fast

Reacting to sudden events with a choice from a menu.

.. code-block:: inform7

   Include Reactable Quips by Michael Martin.
   Use no scoring.

   The Playground is a room. "This grassy field is perfect for all kinds of sports. Something's happening off to the east."
   East of the playground is the Pitcher's Mound.

   Table of Quip Texts (continued)
   quip	quiptext
   Sudden Event	"As you walk over to the pitcher's mound, you hear a shout and something flies right at your face!"
   Victory	"You quickly raise your hand and pluck the missile out of the air. Looking at it closely, you see that it is a fabulous gem!"
   Evasion	"You expertly duck and the missile flies over your head, landing somewhere in the playground from whence you came."

   Table of Quip Followups (continued)
   quip	option	result
   Sudden Event	"Catch it"	Victory
   Sudden Event	"Duck it"	Evasion

   The fabulous gem is a thing. The description is "Shiny!"
   After quipping when the current quip is Victory: now the player holds the fabulous gem.
   After quipping when the current quip is Evasion: now the fabulous gem is in the Playground.

   Every turn: If the player carries the fabulous gem, end the story finally saying "You're fantastically wealthy!"

   Assault is a scene. Assault begins when the location is the Pitcher's Mound. When Assault begins: deliver the Sudden Event quip. Assault ends when the fabulous gem is not off-stage.

   Test catch with "e / 3 / 1".
   Test evade with "e / e / repeat / 2 / w / get gem".

Room Description Supporter Bugfixes
===================================

**Author:** Nathanael Nerode | **Version:** 1.0.220523

Fixes some issues in Standard Rules related to printing room descriptions with
enterable supporters.

**Documented usage:**

.. code-block:: inform7

   if the item is locale-supportable and the tabletop does not conceal the item

Singing Reloaded
================

**Author:** Shin | **Version:** 1

Singing as defined in Version 2/090402 of the Standard Rules by Graham Nelson.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Standard Rules Dead Code Removal
================================

**Author:** Nathanael Nerode | **Version:** 2.0.220521

Reduce the size of games using Room Description Control by removing unused
Standard Rules material. This version tested with Inform v10.1.

**Documented usage:**

.. code-block:: inform7

   2.0.220521: Update to Inform v10.1, which renamed sections of the Standard Rules, largely for the better.
   1: First version.

Title Page
==========

**Author:** Gavin Lambert | **Version:** 1.0.1

Provides an intro screen to the story, offering an image and menu.

**Basic example:** Simple Defaults

Basic title page

.. code-block:: inform7

   Include Title Page by Gavin Lambert.

   Limbo is a room.

Trinity Inventory
=================

**Author:** Mikael Segercrantz | **Version:** 5.1

Provides a framework for listing inventories in natural sentences, akin to
Infocom's game Trinity. Separates carried and worn objects, followed by objects
that contains other objects. What's listed in the third section is customizable
via a rulebook. Objects can be marked as not listed when carried or worn as well
as marked as having their contents listed in the inventory when they're empty.
This extension is based upon the extension Written Inventory by Jon Ingold.

**Basic example:** Trinity

Demonstrating the use of items not listed in the inventory and containers listed
even if empty.

.. code-block:: inform7

   Include Version 4 of Trinity Inventory by Mikael Segercrantz.

   Palace Gate is a room. "A tide of perambulators surges north along the crowded Broad Walk. Shaded glades stretch away to the northeast, and a hint of color marks the western edge of the Flower Walk."

   The player wears a vacation outfit. The vacation outfit is unlisted when worn.
   The player wears a wristwatch. Understand "watch" as the wristwatch.
   A container called your pocket is part of the vacation outfit. Your pocket is empty-listed.
   A credit card is in your pocket.
   A seven-sided coin is in your pocket. Understand "seven" and "sided" as the seven-sided coin.

   The seconds count is a number which varies. The seconds count is 0.

   The realistic time rule is listed instead of the advance time rule in the turn sequence rulebook.

   This is the realistic time rule:
   	now the seconds count is the seconds count + 15;
   	while the seconds count is at least 60:
   		now the seconds count is the seconds count - 60;
   		now the time of day is the time of day + 1 minute.

   The description of the wristwatch is "[if the hours part of the time of day is greater than 12][the hours part of the time of day - 12][otherwise][the hours part of the time of day][end if]:[if the minutes part of the time of day is less than 10]0[end if][the minutes part of the time of day]:[if seconds count is less than 10]0[end if][seconds count] [if the hours part of the time of day is at most 11]am[otherwise]pm[end if]."

   When play begins:
   	say "Sharp words between the superpowers. Tanks in East Berlin. And now, reports the BBC, rumors of a satellite blackout. It's enough to spoil your continental breakfast.

   But the world will have to wait. This is the last day of your $599 London Getaway Package, and you're determined to soak up as much of that authentic English ambience as you can. So you've left the tour bus behind, ditched the camera and escaped to Hyde Park for a contemplative stroll through the Kensington Gardens."

   Test me with "i / x watch / take coin / i / x watch / take card / i".

Undo Output Control
===================

**Author:** Nathanael Nerode | **Version:** 6.0.220529

Provides hooks into UNDO processing, including multiple ways to suspend UNDO
temporarily, to place limitations on UNDO (such as allowing only one UNDO in a
row), to undo the current turn from code, and to control when the game state is
saved. Using the latter, we can effectively control which turn UNDO returns us
to. Also allows the story to edit a blank command before analyzing it. Updated
to Inform 10.1.

**Basic example:** Mynah Undo

Presents report rules that reproduce Inform's default output.

.. code-block:: inform7

   The story author is "Erik Temple".
   Include Undo Output Control by Nathanael Nerode.

   Laboratory is a room. The pen, the vial, the bunsen burner, the beaker, the banana, and the viol are in Laboratory.

   Report undoing an action:
   	say "[bold type]";
   	say "[Location]" in upper case;
   	say "[roman type]";
   	say "[line break]";
   	say "[bracket]Previous turn undone.[close bracket][line break]";
   	rule succeeds.
   	
   Report prevented undo:
   	say "The use of UNDO is forbidden in this game.";
   	rule succeeds.
   	
   Report nothing to be undone failure:
   	say "[bracket]You can't [quotation mark]undo[quotation mark] what hasn't been done![close bracket][line break]";
   	rule succeeds.
   	

   Section (for Glulx only)

   Report interpreter undo failure:
   	say "[bracket]You cannot [quotation mark]undo[quotation mark] any further.[close bracket][line break]";
   	rule succeeds.


   Section (for Z-machine only)

   Report interpreter undo failure:
   	say "[quotation mark]Undo[quotation mark] failed. [bracket]Not all interpreters provide it.[close bracket][line break]";
   	rule succeeds.

Unknown Word Error
==================

**Author:** Mike Ciul | **Version:** 2.2

Provides Infocom-style parser messages such as 'I don't know the word 'kludge'.'

**Basic example:** Ignorance is Bliss

A brief test of this extension.

.. code-block:: inform7

   Include Unknown Word Error by Mike Ciul.

   The Conference Chamber is a room. In the Conference Chamber is a table. On the table is a treaty.

   Test me with "examine non-proliferation treaty".

Unsuccessful PC Attempt
=======================

**Author:** Ron Newcomb | **Version:** 2

Will run the Unsuccessful Attempt By rules for all characters, including the
player. Also silences the library messages printed by the built-in Check rules.

**Basic example:** "Road Test"

Success and failure on the road to nowhere.

.. code-block:: inform7

   Include Unsuccessful Pc Attempt by Ron Newcomb.

   Unsuccessful attempt by an actor doing something: say "Oomph!  [Actor] can't because of the [reason the action failed]."

   The block sleeping rule is not listed in any rulebook.

   Check an actor sleeping (this is the gravel road rule): say "(Can't sleep here!)" instead.
   Check an actor waiting (this is the kinda already doing rule): say "(Waiting is a little too easy.)"; rule succeeds.

   Carry out an actor sleeping: say "[Actor] sleeps quietly."
   Carry out an actor waiting: say "[Actor] waits quietly."

   Sleeping is being silly.

   A gravel road is a room. Bob is a man in a gravel road. A stop sign is fixed in place in a gravel road. Persuasion: rule succeeds.

   Test me with "sleep / bob, sleep / wait / bob, wait / take stop sign / bob, take stop sign ".

Written Inventory
=================

**Author:** Leonardo Boselli | **Version:** 3.2

Just Version 3 of Written Inventory by Jon Ingold made adaptive. Provides a
framework for listing inventories in natural sentences. Separates carried and
worn objects, followed by objects that contains other objects. What's listed in
the third section is customisable via a rulebook.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

####################################
Saving, Files & Persistence
####################################

Autosave (for Glulx only)
=========================

**Author:** Daniel Stelzer | **Version:** 2.0.231013

Allows the programmer to save and restore from an autosave file without the user
being aware of it.

**Documented usage:**

.. code-block:: inform7

   autorestore the game

Flexible Logger
===============

**Author:** Peter Orme | **Version:** 3.3

A logging tool for I7 that lets you log to transcript and (with Glulx) to file

**Basic example:** Hello log

A minimal example. Just include and "debug", "warn" etc.

.. code-block:: inform7

   Include Flexible Logger by Peter Orme.

   There is a room. 

   When play begins: 
   	debug "Hello log!";
   	warn "This is a warning.";

Guide Mode
==========

**Author:** Wade Clarke | **Version:** 4.0

Enables you to add a guide mode to your game. The guide mode walks the player
through the game one command at a time. The author creates the table of commands
for the game to supply. The player can accept and enter each displayed command
by pressing ENTER. If the player types a different in world command, guide mode
is paused (and no more guide commands are displayed) allowing the player to
experiment or explore. The player can leave guide mode by typing GUIDE OFF.
Otherwise, when they UNDO during pause mode, they will be rewound to the moment
just before they paused, and put back in guide mode.

**Basic example:** The Sawyer Place

A short adventure demonstrating most features of guide mode. The game has one
randomised element which is figured into its guide: Each game, the target safe
is randomly located in one of three upstairs rooms. The other two rooms bring
instant death. A clue downstairs informs the player which is the correct room.
The game's guide makes sure the player will have read the clue before
encountering the numbered rooms, then uses a pre-command rule in its table of
guidance to jump to the correct spot in the guide so that the player enters the
correct room. In other words, the commands dispensed near the end of the guide
automatically cater for the randomised content.

.. code-block:: inform7

   Include Guide Mode by Wade Clarke.

   When play begins:
   	now the autosave filename is "sawyerauto";

   When play begins (this is the ask player if they want guide mode rule):
   	follow the invite player to use guide mode rule;

   room-with-the-safe-in-it is initially 0.

   When play begins:
   	now the room-with-the-safe-in-it is a random number between 1 and 3;

   Description of the player is "Having to wear a suit is a con of the private investigator's trade.".

   player carries a derringer.
   Description of derringer is "A small pistol with two barrels.".

   Understand "help" as requesting help.
   requesting help is an action out of world applying to nothing.

   Carry out requesting help:
   	say "[italic type]Sawyer's safe must be around here somewhere. But you've heard there are also two booby-trapped false safes.[roman type][line break]";


   Vestibule is a room. "You're in the vestibule of Old Lady Sawyer's decrepit mansion. The front door is south, but you're not ready to leave yet. Other doors go west, north and east.".

   Check going south in vestibule:
   	instead say "You're not ready to leave this house yet.";


   Slanting Corridor is west of vestibule. "You're in a corridor that slants down to the west. You've got a bad feeling about it. The vestibule is east.".

   Smelly Corridor is west of slanting corridor. "The corridor here smells foul. The smell seems to be coming from the west. The corridor slants upwards to the east."

   Rank Corridor is west of smelly corridor. "The corridor here smells rank. Decaying flesh rank. There's a bloated wooden door to the west. Your internal sense is screaming at you not to continue, but to go back east.".

   a circuit board is fixed in place in rank corridor. "You see a circuit board on the wall.".
   Description of circuit board is "The circuit board is old and arcane, but according to scratchings on the wall beside it, the power is connected to rooms [if room-with-the-safe-in-it is 1]two and three upstairs, but not room one[otherwise if room-with-the-safe-in-it is 2]one and three upstairs, but not room two[otherwise]rooms one and two upstairs, but not room three[end if]. Could it be that the rooms with power are the rooms with booby-traps?".

   Instead of switching off circuit board:
   	say "You can't work out how. This thing's so old and bizarre you might electrocute yourself if you mess with it.".


   Death Pit is west of Rank Corridor.

   After going to death pit:
   	end the story saying "As you step through the doorway, your feet go straight through a termite-ridden floor. You crash down into Sawyer's infamous punji-stake-lined death pit. Mortally wounded, you join the vermin and the other dead."


   Kitchen is east of Vestibule. "You're in a mouldy kitchen. A door leads west.".

   some cobwebs are in kitchen. "Cobwebs cover one wall.".
   Understand "cobweb/web/webs" as cobwebs.

   a wrench is in kitchen. "A wrench lies in the dust.".

   a cracker is in kitchen. "There's a dessicated diet cracker by the sink.".
   Understand "dessicated/diet" as cracker.

   Instead of eating cracker:
   	say "Maybe if you were starving, you'd eat this cracker that's been sitting in a dead woman's kitchen for months. But you're not starving.".

   Description of cobwebs is "They're so thick, you can't see through them.".

   Instead of taking cobwebs:
   	say "You tear the cobwebs aside, revealing a pentagram painted on the wall... in blood!";
   	now pentagram is in kitchen;
   	now cobwebs are nowhere.

   a pentagram is fixed in place. "There's a bloody pentagram on the wall. It means something, obviously, and presumably that something is not good.".


   Hall is north of vestibule. "You're in a dingy hall with chequerboard tiling. The vestibule is south and a staircase leads up.".


   a gallery-room is a kind of room.

   Gallery is a gallery-room. It is up from hall. "You're in a mahogany gallery. Stairs lead down to the hall. The gallery extends north and south and there's a door to the west with a brass '2' on it.".

   Gallery South is a gallery-room. It is south from gallery. "You're at the south end of the gallery. There's a door to the west with a brass '3' on it.".

   Gallery North is a gallery-room. It is north from gallery. "You're at the north end of the gallery. There's a door to the west with a brass '1' on it.".


   a safe is a closed, locked, openable fixed in place container.
   Description of safe is "Okay, here's Sawyer's safe. But what's the combination?".

   Check opening safe:
   	end the story saying "You don't know the combination to the safe, but working out what it is will be your next adventure.";


   A safe-room is a kind of room. The description of a safe-room is usually "You're in room [safe-id of the item described]. There's a [safe] in the west wall. A door east goes back to the gallery.".

   A safe-room has a number called safe-id.

   Room 1 is a safe-room. It is west of gallery north. The safe-id of room 1 is 1.
   Room 2 is a safe-room. It is west of gallery. The safe-id of room 2 is 2.
   Room 3 is a safe-room. It is west of gallery south. The safe-id of room 3 is 3.

   Carry out going to a safe-room:
   	now safe is in the room gone to;

   After going to a safe-room:
   	if room-with-the-safe-in-it is not safe-id of the location:
   		end the story saying "When you touch the door handle to room [safe-id of the location], you hear a mechanical snapping sound in the adjacent wall. You wonder for a moment whether you've triggered one of Sawyer's booby-traps. A massive explosion confirms it.";
   	otherwise:
   		continue the action;



   table of guidance (continued)
   prose(text)	display-prose(text)	pre-command-rule(a rule)
   "x me"	--	--
   "i"	--	--
   "x derringer"	--	--
   "s"	--	--
   "help"	--	--
   "e"	--	--
   "x webs"	--	--
   "get webs"	--	--
   "l"	--	--
   "get wrench"	--	--
   "eat cracker"	--	--
   "w"	--	--
   "w"	--	--
   "w"	--	--
   "w"	--	--
   "x board"	--	--
   "e"	--	--
   "g"	--	--
   "g"	--	--
   "n"	--	--
   "u"	--	--
   "n"	--	--
   "s"	--	--
   "s"	--	go to the safe room rule
   "n"	--	--
   "n"	--	--
   "w"	--	--
   "x safe"	--	--
   "open safe"	--	--

   table of whitelisted commands (continued)
   prose(text)
   "help"

   This is the go to the safe room rule:
   	if room-with-the-safe-in-it is:
   		-- 3:
   			guidejump 3;[after the current guide command is executed, the guide will continue from the table entry THREE entries below this rule]
   		-- 2:
   			guidejump 2;[after the current guide command is executed, the guide will continue from the table entry TWO entries below this rule]

Highscores (for Glulx only)
===========================

**Author:** Dannii Willis | **Version:** 1.2

Record and review highscores to an external file

**Basic example:** Highscores Example

.. code-block:: inform7

   The Records Room is a room.

   Include Highscores by Dannii Willis.

   After printing the banner text:
   	say "Checksum [the game checksum][line break]";

   The File of Highscores is called "testscores".

   Recording a score is an action applying to one number.
   Understand "record [a number]" as recording a score.

   Carry out recording a score:
   	record score of the number understood and review highscores from The File of Highscores;

####################################
Story Structure, Choice & Narrative
####################################

Extended Banner
===============

**Author:** Gavin Lambert | **Version:** 5.0.1

More control over what is printed in a banner, including an easily-included
copyright line.

**Basic example:** Defaults

A simple demonstration of the defaults.

.. code-block:: inform7

   Include Extended Banner by Gavin Lambert.

   There is a room.

Extended Banner
===============

**Author:** Nathanael Nerode | **Version:** 6.0.220604

More control over what is printed in a banner, including an easily-included
copyright line.

**Basic example:** A Simple Copyright

A copyright and license statement

.. code-block:: inform7

   Include Extended Banner by Nathanael Nerode.

   The story copyright string is "2005-6".
   The story rights statement is "Released under the Creative Commons

Game Ending Reloaded
====================

**Author:** Shin | **Version:** 1

Game Ending as defined in Version 2/090402 of the Standard Rules by Graham
Nelson.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Randomness
==========

**Author:** Mikael Segercrantz | **Version:** 2.2

Random number generation using a simple seedable pseudorandom number generator.

**Documented usage:**

.. code-block:: inform7

   the next random number

Recorded Endings (for Glulx only)
=================================

**Author:** Emily Short | **Version:** 5

Records the endings the player encounters in multiple play-throughs to an
external file; then adds an ENDINGS option to the final question to allow the
player to review which endings he has seen so far.

**Basic example:** Reincarnation

We have a vial of poison that the player recognizes only on the second
playthrough.

.. code-block:: inform7

   Include Recorded Endings by Emily Short.

   The File of Conclusions is called "examplecon".

   The Cloudy Chamber is a room. It contains a wooden table. On the wooden table is a vial.

   The description of the vial is "It is full of a delicious-looking golden liquid."

   Instead of smelling the vial: 
   	say "It smells like honey wine."

   Rule for printing the name of the vial when "Death by poison" is a used ending:
   	say "vial of poison".
   	
   Understand "poison" or "of poison" as the vial when "Death by poison" is a used ending.

   Instead of drinking the vial:
   	if "Death by poison" is a used ending:
   		say "A chill comes over you as you consider it, as though you were being warned by a previous incarnation from another lifetime: this is foul poison.";
   	otherwise:
   		say "You lift the vial to your lips and throw it back. The flavor is sweet on your tongue, but the effects are nearly instant...";
   		record "Death by poison" as an ending;
   		end the story saying "You have died by poison".

Small Kindnesses
================

**Author:** Aaron Reed | **Version:** 13.2

Provides a number of small interface improvements for players, understanding
commands like GO BACK and GET IN, an EXITS command which automatically runs
after failed movement, a USE verb, and more. Compatible with Modified Exit and
Approaches by Emily Short, Keyword Interface by Aaron Reed, and Implicit Actions
by Eric Eve.

**Basic example:** Checkup

A small example illustrating the extension's functionality.

.. code-block:: inform7

   Include Small Kindnesses by Aaron Reed.

   Sidewalk is a room. The Waiting Room is inside from Sidewalk. The Dentist's Office is east of Waiting Room. A reclined chair is a fixed in place enterable supporter in Office. "You see a comfy chair here." The player wears a backpack. The backpack is open and openable. In the backpack is a magazine.    

   Test me with "look at sidewalk / in / e / exit / n / e / get in chair / w / go back / eat chair / sit on chair / use backpack".

Story Mode
==========

**Author:** Drew Cook | **Version:** 2.2.0

Provides an optional mode in which the game automatically steps through a
walkthrough. At any time, players can pause the guide and play independently. At
any future point, players can return to the walkthrough in progress. This is a
'safe' mode of play in which neither the walkthrough nor the game world can be
disrupted. The primary design goal of story mode is improved accessibility,
though it has potential as a tutorial feature.

**Documented usage:**

.. code-block:: inform7

   wait for any key.

####################################
Testing, Debugging & Development
####################################

Autoundo for Object Response Tests
==================================

**Author:** Mike Ciul | **Version:** 1

Tests objects just like Juhana Leinonen's extension, but does an UNDO after each
test.

**Basic example:** Undropped

items that can't be restored to their original state by dropping them

.. code-block:: inform7

   Include Autoundo for Object Response Tests by Mike Ciul.

   Test is a room.

   The glass box is a transparent closed openable container in Test.

   The piece of gum is a thing in Test.

   Check dropping the gum:
   	say "It sticks to your fingers and won't let go.";
   	stop the action.

   After dropping the glass box:
   	say "It smashes into a million pieces.";
   	Now everything in the glass box is in the location;
   	remove the glass box from play.

   test me with "autoundo actions/analyze box/analyze gum/autoundo turns/analyze box/analyze gum/i/l/autoundo off/analyze box/analyze gum/i/l"

Debug Files (for Glulx only)
============================

**Author:** Juhana Leinonen | **Version:** 2

A development tool for saving debugging information to an external text file
during beta testing.

**Basic example:** Bear Hunter

An example where some information of the game mechanics is saved to the debug
file.

.. code-block:: inform7

   Use debug files.

   The glacier is a room. A bipolar bear is a male animal in the glacier. The bipolar bear can be manical or depressed. The description of the bear is "The bipolar bear looks [if manical]like he's full of life[otherwise]quite depressed[end if]."

   A person has a number called hit points. The hit points of a person is usually 10.

   Every turn when a random chance of 1 in 3 succeeds:
   	if the bear is depressed:
   		now the bear is manical;
   		debug "The bear has a manic episode.";
   	otherwise:
   		now the bear is depressed;
   		debug "The bear is now depressed."

   Instead of attacking the depressed bear:
   	say "You strike the bear with all your strength.";
   	decrease the hit points of the bear by a random number between 1 and 5;
   	debug "Bear's hit points reduced to [hit points of the bear].";
   	if the hit points of the bear is less than 1:
   		say "[line break]The mighty bipolar bear falls and you get another victory.";
   		end the game in victory;
   	otherwise:
   		say "[line break]'Go ahead. Life's not worth it anyways,' the bear says."

   Instead of attacking the manical bear:
   	say "'Oh no you don't!' the bear roars and slams you with his mighty white paw. 'There's nothing that could stop me today!'";
   	decrease the hit points of the player by a random number between 1 and 5;
   	debug "Player's hit points reduced to [hit points of the player].";
   	if the hit points of the player is less than 1:
   		say "[line break]The Great Bipolar Bear of the North proves to be stronger than you.";
   		end the game in death.

   Test me with "x bear/attack bear/g/g/g/g/g".

Debug Tags
==========

**Author:** Michael Kielstra | **Version:** 1

Take quick notes about what needs doing: bugs, ideas, et cetera. Helpful for
debugging.

**Basic example:** The Lab

A basic example.

.. code-block:: inform7

   Include Debug Tags by Michael Kielstra.

   The Lab is a room.  The lab bench is in the Lab.  The chemical box is in the lab.  It is an openable open container.  The chemical phial is in the chemical box.

   IMPLEMENT CHEMICAL MIXING/ALCHEMY SYSTEM is a TODO.
   MAYBE ADD SOME PHENOLPHTHALEIN - I LOVE PHENOLPHTHALEIN is an IDEA.

   PLAYER CANNOT PUT PHIAL ON LAB BENCH is a STOPSHIP.
   	
   Test me with "take phial / put chemical phial on lab bench".

Nathanael's Debug Tools
=======================

**Author:** Nathanael Nerode | **Version:** 3.0.220522

Miscellaneous stuff I like to have built in when debugging and programming, but
would never want to relase.

**Documented usage:**

.. code-block:: inform7

   Use startup rules tracing

Object Response Tests
=====================

**Author:** Juhana Leinonen | **Version:** 7

A development tool for testing all actions on any given object - or one action
on all objects - at once to see whether the game's responses are sensible.

**Basic example:** Camp Fire

An example of basic use of the extension

.. code-block:: inform7

   Include Object Response Tests by Juhana Leinonen.

   The Camp is a room.

   The bonfire is in the Camp. It is fixed in place. The description is "The bonfire is blazing hot."

   Alice is a woman in the Camp.

   Instead of touching the bonfire:
   	say "Ow! You almost burn your fingers."

   Test me with "analyze bonfire/try touching/analyze nounless/actor is Alice/analyze bonfire".

####################################
Text, Prose & Output
####################################

Clues and Conversation
======================

**Author:** Brian Rushton | **Version:** 5

A simple system for building conversations.

**Basic example:** The Detective

Having a single clue with no specific target.

.. code-block:: inform7

   Include Clues and Conversation by Brian Rushton.

   The Study is a room. Parlor is north of the Study.

   Watson is a man in the Parlor. The description of Watson is "Watson is interested in everything you have to say."

   When play begins:
   	deliver Ash;
   	
   Ash is a clue. The preview of Ash is "The ash was from a cigar manufactured in Greenland.".

   The TargetResponse of Ash is "'This is a Greenland cigar', you shout.

   'Hurrah!' says Watson."

   Test me with "T / say Ash / N / say ash / T"

Contextual Descriptions
=======================

**Author:** Jeff Nyman | **Version:** 1.3

Provides a mechanism for contextually shifting descriptions.

**Basic example:** A Walk Through the Park

.. code-block:: inform7

   Include Contextual Descriptions by Jeff Nyman.

   Palace Gate is a room. "[if unvisited]Palace Gate is a street running north to south leading up to Kensington Gardens. It was previously part of the Gloucester Road, which is just to the south. According to the guidebook, Gloucester Road was named after Maria, Duchess of Gloucester and Edinburgh who apparently built a house there in 1805.[else]This is the Palace Gate street, leading into Kensington Gardens, with the north taking you to [summarize the Broad Walk] and east taking you to [summarize the Flower Walk]."

   Broad Walk is a room. "A brooding statue of Queen Victoria faces east, where the waters of the Round Pond sparkle in the afternoon sun. Your eyes follow the crowded Broad Walk north and south until its borders are lost amid the bustle of perambulators. Small paths curve northeast and southeast between the trees."

   The unvisited summary of the Broad Walk is "what appears to be the crowded Broad Walk".

   The visited summary of the Broad Walk is "what you have seen is the very crowded Broad Walk".

   Flower Walk is a room. "Gaily colored flower beds line the walks bending north and west, filling the air with a gentle fragrance. A little path leads northeast, between the trees.[paragraph break]The spires of the Albert Memorial are all too visible to the south. Passing tourists hoot with laughter at the dreadful sight; nannies hide their faces and roll quickly away."

   The unvisited summary of the Flower Walk is "what appears to be the slightly less crowded Flower Walk".

   The visited summary of the Flower Walk is "what you have seen is the slightly less crowded Broad Walk".

   Broad Walk is north of Palace Gate.
   Flower Walk is east of Palace Gate.

   Test me with "look / north / south / impressions / east / west".

Conversation Responses
======================

**Author:** Eric Eve | **Version:** 7

Provides a meaning for defining responses to conversational commands (such as
ASK FRED ABOUT GARDEN) as a series of rules.

**Basic example:** Bob's Lost Wallet

A brief conversation illustrating the use of response rules.

.. code-block:: inform7

   Include Conversation Responses by Eric Eve.

   The Hall is a Room. "As befits a grand old manor house, the hall is imposingly large, with acres of polished wooden floorboards and scores of ancient family portraits hung about the walls."

   Some ancient family portraits are scenery in the Hall.
   Understand "ancestors" as the ancient family portraits.

   Bob is a man in the Hall. "Bob is standing in the middle of the hall, looking rather worried."

   After saying hello to Bob:
   say "'Hello there, Bob!'[paragraph break]'Good morning,' he replies."

   Response of Bob when asked about Bob:
   say "'[one of]How are you today? You look worried!' you remark.[paragraph break]'I've lost my wallet,' he tells you[make lost wallet known][or]Are you okay - apart from your wallet?' you ask.[paragraph break]'Fine, but I'm so worried about my wallet!' he replies[stopping]."

   Response of Bob when asked about the lost wallet:
   say "'Where did you last see your wallet?' you ask.[paragraph break]'I can't remember,' he replies."

   Response of Bob when asked-or-told about "[theft]" and the lost wallet is known:
   say "'[one of]Could your wallet have been stolen, do you think?' you ask.[paragraph break]'I don't know,' he answers miserably[or]Have you tried telling the police?' you suggest.[paragraph break]'No, I'd feel such a fool if it just turned up,' he replies[stopping]."

   Response of Bob when saying sorry and the lost wallet is known:
   say "'Well, I'm sorry you can't find your wallet,' you say.[paragraph break]'So am I,' he tells you."

   Response of Bob when asked-or-told about the ancient family portraits:
   say "'[one of]Who are all those people in the portraits?' you ask.[paragraph break]'Oh, just my ancestors. I expect half of them were hung for sheep-stealing,' he replies[or]I don't think your ancestors look that disreputable,' you remark.[paragraph break][make lost wallet known]'Never mind my ancestors - it's my wallet I'm worried about!' he replies[stopping]."	

   Response of Bob when shown the silver dollar:
   say "'Is this any good to you?' you ask.[paragraph break]'One dollar?' he asks, 'Thanks, but no thanks. It's not the cash I'm so worried about, it's the credit cards!'"

   The silver dollar is carried by the player.

   The lost wallet is a thing. 

   Understand "bob's" or "his" as the lost wallet.

   Understand "theft" or "thief" or "stolen" or "police" as "[theft]".

   Test me with "Ask bob about himself/a bob/a wallet/a portraits/a ancestors/a theft/t police/show dollar"

Conversational Defaults
=======================

**Author:** Eric Eve | **Version:** 3

Provides a set of rules to facilitate defining default conversational responses
for different conversational commands targeted at various NPCs. This extension
requires Conversation Framework.

**Basic example:** Sisko's Briefing

A brief conversation with defaults.

.. code-block:: inform7

   Include Conversational Defaults by Eric Eve.

   Captain Sisko's Office is a Room.
   "Behind the desk a pair of large windows overlook the stars that seem to surround the wormhole."

   The large desk is a scenery supporter in Captain Sisko's Office.
   	
   Benjamin Sisko is a man in Captain Sisko's Office. "Captain Sisko is seated behind his desk."
   Understand "ben" or "captain" as Benjamin Sisko.

   After quizzing Sisko about the dominion war:
   say "'It's not going as well as I'd like; we're taking far too many casualties,' he tells you."

   After quizzing Sisko about Gul Dukat:
   say "'He's a very evil man,' Sisko opines."

   After quizzing Sisko about Sisko:
   say "'I am quite well, thank you,' he assures you."

   After informing Sisko about Quark:
   say "'Up to his usual tricks, no doubt,' he nods."

   default ask-tell response for Sisko:
   say "'Let's talk about that some other time,' he suggests."

   default ask-for response for Sisko:
   say "'I'm afraid I can't help you with that just now,' he tells you."

   default yes-no response for Sisko:
   say "'I wasn't aware I had just asked you something,' Sisko remarks."

   The dominion war is a familiar thing.
   Gul Dukat is a familiar man.
   Quark is a familiar man.

   Test me with "a sisko/a war/a quark/t quark/ask for promotion/a dukat/a bashir/t dax"

Description Decay
=================

**Author:** Jeff Nyman | **Version:** 1.3

Provides a mechanism for allowing description levels to change based on number
of visits

**Basic example:** Description of Diminishing Returns

.. code-block:: inform7

   Include Rideable Vehicles by Graham Nelson.
   Include Contextual Descriptions by Jeff Nyman.
   Include Description Decay by Jeff Nyman.

   A thing can be examined or unexamined.
   A thing is usually unexamined.

   After examining something:
   	now the noun is examined.

   Palace Gate is a room. "Palace Gate is a street running north to south leading up to Kensington Gardens. It was previously part of the Gloucester Road, which is just to the south. According to the guidebook, Gloucester Road was named after Maria, Duchess of Gloucester and Edinburgh who apparently built a house there in 1805.[paragraph break]A tide of baby strollers -- or perambulators, as they call them here -- surges north along what becomes the crowded Broad Walk. Shaded glades stretch away to the northeast and a hint of color marks the western edge of what the guidebook says is the Flower Walk."

   The summary description of Palace Gate is "The Palace Gate street, leading into Kensington Gardens, with the north taking you to [summarize the Broad Walk] and east taking you to [summarize the Flower Walk]."

   The visited summary of Palace Gate is "the Palace Gate entrance to the park".

   Broad Walk is a room. "A brooding statue of Queen Victoria faces east, where the waters of the Round Pond sparkle in the afternoon sun. Your eyes follow the crowded Broad Walk north and south until its borders are lost amid the bustle of perambulators. Small paths curve northeast and southeast between the trees."

   The summary description of Broad Walk is "The statue of Queen Victoria looks out over the crowds as they bustle to various areas of the park."

   The unvisited summary of the Broad Walk is "what appears to be the crowded Broad Walk".
   The visited summary of the Broad Walk is "what you have seen is the very crowded Broad Walk".

   Flower Walk is a room. "Gaily colored flower beds line the walks bending north and west, filling the air with a gentle fragrance. A little path leads northeast, between the trees.[paragraph break]The spires of the Albert Memorial are all too visible to the south. Passing tourists hoot with laughter at the dreadful sight; nannies hide their faces and roll quickly away."

   The summary description of Flower Walk is "The walk lined with flowers. Northwest leads to [summarize the Wabe]. West takes you to [summarize Palace Gate] and north takes you to [summarize Lancaster Walk]."

   The unvisited summary of the Flower Walk is "what appears to be the slightly less crowded Flower Walk".
   The visited summary of the Flower Walk is "what you have seen is the slightly less crowded Broad Walk".

   A soccer ball is in Flower Walk.

   The initial appearance of the soccer ball is "You can see a soccer ball half-hidden among the blossoms."

   Lancaster Walk is a room. "An impressive sculpture of a horse and rider dominates this bustling intersection. The Walk continues north and south; lesser paths curve off in many directions.[paragraph break]A broad field of grass, meticulously manicured, extends to the east. Beyond it you can see the Long Water glittering between the trees."

   The summary description of Lancaster Walk is "[if the sculpture is proper-named]The[else]An[end if] impressive [sculpture] [if the sculpture is not proper-named]of a horse and rider [end if]is a focal point of the busy walk."

   The unvisited summary of Lancaster Walk is "what appears to be a long, crowded walkway".
   The visited summary of Lancaster Walk is "the crowded intersection of Lancaster Walk".

   A sculpture is in Lancaster Walk.

   The description of the sculpture is "[if unexamined][paragraph break]According to the plaque, the sculpture is called [italic type]Physical Energy[roman type]. According to the guidebook, it's the work of a British artist named George Frederic Watts. Apparently 'physical energy' is an allegory of the human need for new challenges, of our instinct to always be scanning the horizon, looking towards the future. A quote from the artist says that it's 'a symbol of that restless physical impulse to seek the still unachieved in the domain of material things'.[else]The [italic type]Physical Energy[roman type] sculpture, which is basically a bronze statue of man on horseback."

   Before examining the sculpture for the first time:
   	now the printed name of the sculpture is "[italic type]Physical Energy[roman type] scultpure";
   	now the sculpture is proper-named;
   	say "Looking at the sculpture, you realize it has a plaque in front of it. [run paragraph on]".

   The Wabe is a room. "This grassy clearing is only twenty feet across, and, unless your eyes deceive, almost perfectly circular. Paths wander off in many directions through the surrounding thicket.[if unvisited][paragraph break]Oddly enough, this location doesn't appear in the guidebook at all.[end if]"

   The summary description of the Wabe is "The oddly circular clearing that the guidebook most definitely does not mention."

   The unvisited summary of the Wabe is "a part of the park that the guidebook doesn't seem to indicate".
   The visited summary of the Wabe is "the odd little area with the sundial".

   Broad Walk is north of Palace Gate.
   Flower Walk is east of Palace Gate.
   Lancaster Walk is north of Flower Walk.
   The Wabe is northeast of Palace Gate and northwest of Flower Walk.

   A person called Floyd is in Palace Gate.

   A perambulator is in Palace Gate.
   The perambulator is fixed in place and pushable between rooms.
   Understand "pram" as the perambulator.

   A bicycle is a rideable vehicle in Palace Gate.
   Understand "bike" as the bicycle.

   Every turn:
   	if the location of Floyd is not the location of the player:
   		let on the path be the best route from the location of Floyd to the location of the player;
   		try Floyd going on the path.

   Test me with "north / south / east / west / look / impressions".

Dice
====

**Author:** David A Wheeler | **Version:** 1.3

Support conventional X d Y dice notation, e.g., 3 d 6 totals 3 six-sided dice.

**Basic example:** Pest Control

Dice in Action

.. code-block:: inform7

   "Pest Control" by David A Wheeler

   Include Dice by David A Wheeler.

   [Significants parts below are derived from the "Randomness" section example "Lanista 1"]

   A person has a number called current hit points.

   The Dragon's Lair is a room. "This is a beautiful airy room."
   An animal called Malevilness the Red Dragon is here.
   The description of Malevilness is "Malevilness the Red Dragon is taller than 3 men, and there's always room in his stomach for one more."

   When play begins:
   	now the current hit points of the player is 5 d 8;
   	now the current hit points of Malevilness is 5 d 8;
   	now the left hand status line is "You: [current hit points of player]";
   	now the right hand status line is "Dragon: [current hit points of Malevilness]".

   Instead of attacking someone:
   	let the damage be 3 d 6;
   	say "You attack [the noun], causing [damage] points of damage!";
   	decrease the current hit points of the noun by the damage;
   	if the current hit points of the noun is less than 0: 
   		say "[line break][The noun] expires!";
   		now the noun is nowhere;
   		end the story finally;
   		stop the action;
   	let the enemy damage be 2 d 4;
   	say "[line break][The noun] attacks you, causing [enemy damage] points of damage!";
   	decrease the current hit points of the player by the enemy damage;
   	if the current hit points of the player is less than 0:
   		say "[line break]You expire!";
   		end the story.

   Test me with "hit dragon / g / g / g".

Distantly Visible Things
========================

**Author:** Marc Von Der Heiden | **Version:** 2.0.220523

Provides flexible handling of things that can be seen in multiple rooms, but -
unlike backdrops - still have one distinct location.

**Basic example:** Manor House

Showing the standard behavior of the Distantly Visible Things extension

.. code-block:: inform7

   Include Distantly Visible Things by Marc Von Der Heiden.

   End of Street is a room. "The road ends at the old manor house which dominates the landscape. The estate is surrounded by a metal fence, but right here a gate opens up to the north onto the property."
   The gate is a scenery thing in End of street. The description is "Nicely ornamented, with the former owner's family crest at the top.". Understand "fence" and "crest" as the gate. 
   	
   Instead of touching the gate, say "Though it's a warm day, the metal feels somehow chilly.".

   The Huge estate is north of End of street. "You are standing on a lawn which would make every gardener happy. The manor house, three storeys tall, stands proudly in front of you. There's a fence around the lawn but a gate to the south leads to the street."
   The lawn is a scenery thing in the estate. The description is "Perfectly trimmed!".
   The mansion is a scenery thing in the estate. Understand "manor" or "house" or "building" as the mansion. The description of the mansion is "From up close, the number of cracks in the masonry make the deterioration of the building more than obvious.".

   The mansion is distantly visible from End of street. The distant description of the mansion is "A beautiful building that dates back to the Victorian era.". 

   The gate is distantly visible from the estate.

   test me with "x manor house / x gate / touch gate / n / x manor house / x gate / touch gate / x lawn / s / x lawn".

Effective Infinity
==================

**Author:** Mike Ciul | **Version:** 1

Provides a system of counting numbers which never go below 0 or above a
specified maximum value. Any numbers above the maximum are considered infinite.

**Documented usage:**

.. code-block:: inform7

   a few

Hiding Under
============

**Author:** Eric Eve | **Version:** 4

Allows things to be hidden under other things, using a many-to-one
underconcealment relation. Can be used either standalone (with basic
functionality) or in conjunction with Underside (to add fuller functionality to
both extensions). Version 3 of Hiding Under avoids using phrases deprecated in
Version 6E59 of Inform.

**Basic example:** Lost Cheque

A simple example of one thing hidden under another.

.. code-block:: inform7

   Include Hiding Under by Eric Eve.

   The Hall is a room.
   "[if unvisited]You know you dropped a cheque here somewhere; the question is where[otherwise]There's not much of interest here, really, apart from that cheque[end if]."

   The doormat is a portable enterable supporter in the Hall.
   "A brown doormat lies by the front door."

   Understand "brown" or "mat" as the doormat.

   The valuable cheque is hidden under the doormat.
   The description is "It's a cheque for ten thousand [if the American dialect option is active]dollars[otherwise]pounds[end if]."

   Understand "check" as the valuable cheque when the American dialect option is active.

   Rule for printing the name of the valuable cheque when the American dialect option is active: say "valuable check".

   Instead of looking under something when the player is on the noun:
     say "You'll have to get off [the noun] first." 

   Instead of placing the valuable cheque under the doormat:
     hide the valuable cheque under the doormat;
     say "You slip the cheque back under the doormat."

   To say find-hidden-under (the doormat - a thing):
      now everything hidden under the doormat is carried by the player;
      say "Under the mat you find [a list of things hidden under the doormat], which you eagerly snatch up."

   Test me with "look under mat/i/x cheque/put cheque under mat/take mat"

Nathanael's Cookbook
====================

**Author:** Nathanael Nerode | **Version:** 6.0.220604

This is just a collection of documentation and worked examples illustrating
various features of Inform. There isn't much in the extension per se, but the
examples in the documentation can be click-pasted in the Inform IDE for
convenience.

**Basic example:** Examine Room

putting the room in scope

.. code-block:: inform7

   Main Street is a room.
   "This is the center of the city, where it all happens!"

   After deciding the scope of an object (called character) (this is the put room in scope rule):
   	Place the location of the character in scope, but not its contents.

   Rule for deciding whether all includes rooms:
   	it does not.

   test me with "examine street/examine main street/take all".

Neutral Standard Responses
==========================

**Author:** Nathanael Nerode | **Version:** 5.0.220521

Replaces misleading, vague, and narratively-voiced parser messages with
instructive, clarifying, and neutral versions, respectively. For Inform 10.1.0.

**Basic example:** Ignorance is Bliss

Test for don't know that word rule (from Unknown Word Error)

.. code-block:: inform7

   Include Neutral Standard Responses by Nathanael Nerode.

   The Conference Chamber is a room. In the Conference Chamber is a table. On the table is a treaty.

   Test me with "examine non-proliferation treaty".

Notepad
=======

**Author:** Jim Aikin | **Version:** 3

A system for creating an in-game notepad that the player can write on.

**Basic example:** Memorabilia

Some objects the player can write in.

.. code-block:: inform7

   Include Notepad by Jim Aikin.

   The Lab is a room.

   The player carries a fish. The description of the fish is "The fish [are] remarkably scaly."

   The player carries a pencil and a piece of chalk.

   The player carries a slate. The slate is a notepad. The description of the slate is "Black." The allowed-pens of the slate is {chalk}.

   The player carries a notebook. The notebook is a notepad. The description of the notebook is "Dog-eared." The allowed-pens of the notebook is {pencil}.

   The foggy mirror is in the Lab. The description is "The mirror [are] thickly coated with condensed steam." The foggy mirror is a notepad. The pen-needed of the foggy mirror is false. The memo of the foggy mirror is "Beware! Ghouls!"

   Test writing with "write message on fish / write message on slate / read slate / drop chalk / add another message to slate / take chalk / add another message to slate".

   Test reading with "read slate / read fish / read mirror / x mirror".

   Test erasing with "erase me from slate / read slate / erase slate / read slate".

   Test copying with "copy mirror to mirror / copy mirror to notebook / drop chalk / copy notebook to slate".

   Test me with "test writing / test reading / test erasing /test copying".

Plugs and Sockets
=================

**Author:** Sean Turner | **Version:** 4.2

System for handling plugs and sockets.

**Basic example:** Home Theatre

Plugging a variety of components with different connections together to watch a
DVD.

.. code-block:: inform7

   Include Plugs and Sockets by Sean Turner

   Section 1 - New plug and socket kinds

   An HDMI-plug is a kind of PS-plug. The PS-type of an HDMI-plug is "HDMI".
   An HDMI-socket is a kind of PS-socket. The PS-type of an HDMI-socket is "HDMI".

   A DVI-plug is a kind of PS-plug. The PS-type of a DVI-plug is "DVI".
   A DVI-socket is a kind of PS-socket. The PS-type of a DVI-socket is "DVI".

   A power-plug is a kind of PS-plug. The PS-type of a power-plug is "power". A power-plug has a truth state called searched state. The searched state of a power-plug is usually false.

   A power-socket is a kind of PS-socket. The PS-type of a power-socket is "power".

   A double-adapter is a kind of thing. Every double-adapter incorporates a power-plug and two power-sockets.

   A hifi-gadget is a kind of thing. Every hifi-gadget incorporates a power-plug.

   Section 2 - A few decisions 

   To decide if the (test-item - a thing) is powered:
   	repeat with item running through the power-plugs:
   		now the searched state of the item is false;
   	let forever be true;
   	while forever is true:
   		if the test-item is the power point:
   			decide yes;
   		let test-plug be a random power-plug which is part of the test-item;
   		if the test-plug is nothing, or the attachment of the test-plug is nothing:
   			decide no;
   		else:
   			if the searched state of the test-plug is true:
   				decide no;
   			now the searched state of the test-plug is true;
   			now the test-item is the holder of the attachment of the test-plug.

   To decide if the audio is connected:
   	if the HDMI cable is inserted into the receiver, and the HDMI cable is inserted into the DVD player, and the holder of the attachment of the HDMI-IN socket is HDMI cable:
   		decide on true;
   	decide on false.

   To decide if the video is connected:
   	if the video converter is inserted into the TV, and the video converter is inserted into the receiver, and the attachment of the HDMI-OUT socket is the green plug:
   		decide on true;
   	decide on false.

   Section 3 - Scenario

   The Home Theatre is a room. "This softly lit and richly carpeted homage to 1970's decor is the perfect place to relax and watch a movie. A store room is to the south."

   A big screen TV is a hifi-gadget. It is here. "A huge 150cm Plasma TV dominates the north wall.". It is fixed in place.
   The description is "Tastelessly huge. The TV is [if the TV is powered]on although nothing is showing.[else]off.".
   Incorporated by it is a DVI-socket.

   A power point is here. It is fixed in place. "Unfortunately the room has only one single power point tucked away in the corner farthest from the TV."
   Incorporated by it is a power-socket.

   Check plugging a PS-inserter into the power point (this is the power-point-too-far rule):
   	if the noun is fixed in place, say "The plug of [the noun] will not reach to [the power point]." instead;
   	if the noun is not the extension cord, say "It would be useless to plug [the noun] into [the power point] when it is so far from the TV." instead. 

   The power-point-too-far rule is listed last in the check plugging it into rulebook.

   A Blu-ray DVD player is a hifi-gadget. It is here. The description is "A state of the art DVD player. In the player is a movie waiting to be watched. The DVD player is [if the DVD is powered]on and the movie is playing.[else]off."
   Incorporated by it is an HDMI-socket.

   A digital receiver is a hifi-gadget. It is here. It is fixed in place.
   The description is "A complex switching mechanism routing various audio visual inputs to the TV and speakers. The speakers are hard-wired into the back of the receiver. On the back of the receiver are two HDMI sockets labeled HDMI-IN and HDMI-OUT.

   The receiver is [if the receiver is powered]on and hums slightly.[else]off.".
   Incorporated by the receiver is an HDMI-socket called the HDMI-OUT socket.
   Incorporated by the receiver is an HDMI-socket called the HDMI-IN socket.

   Some speakers are scenery. They are here.

   The Store room is south of the Home Theatre.

   An extension cord is here. The description is "5 metres of sturdy electrical cord.". The indefinite article is "an".
   Incorporated by it is a power-plug and a power-socket.

   A video converter cable is here. The description is "It converts from an HDMI source to a DVI destination - useful when only the video component of the signal is required. The male DVI plug is red and the male HDMI plug is green.".
   Incorporated by the cable is a DVI-plug called the red plug.
   Incorporated by the cable is an HDMI-plug called the green plug.

   An HDMI cable is here. Incorporated by it are two HDMI-plugs. The indefinite article is "an". The description is "Connects two HDMI devices for video and sound. The two male connectors are indistinguishable.".

   A cream double adapter is a double-adapter. It is here.
   A white double adapter is a double-adapter. It is here.

   Section 4 - Victory condition

   Every turn:
   	let power flowing be true;
   	repeat with item running through hifi-gadgets:
   		unless the item is powered:
   			now power flowing is false;
   	if power flowing is true, and the audio is connected, and the video is connected:
   		say "Ahh. Now you can relax and watch the movie.";
   		end the story saying "You have won.";
   	else:
   		if the receiver is powered, and the DVD is powered, and the audio is connected:
   			say "You can hear the movie but you can't see any picture!".


   Section 5 - Testing

   test me with "s/get all/n/plug tv into white/plug dvd into white/plug white into cream/plug receiver into cream/plug cream into cord/plug cord into point/plug hdmi into receiver/plug hdmi into dvd/plug video into receiver/x green/x red/plug video into tv/unplug video from receiver/unplug hdmi from receiver/plug hdmi into hdmi-in/plug video into hdmi-out".

   test errors with "plug tv into point/plug tv into receiver/s/get all/n/plug cord into point/s/plug hdmi into cream/unplug cord from point/plug cord into cord/unplug cord/plug tv into white/plug receiver into white/ plug cream into white/unplug tv/plug red plug into receiver/plug green plug into receiver/plug video cable into tv".

Response Assistant
==================

**Author:** Aaron Reed | **Version:** 1

Adds some helpful testing commands for changing default responses.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Snippetage
==========

**Author:** Dave Robinson | **Version:** 2

Some functions for setting and use of snippets (parts of the player's command).

**Basic example:** Pedantic Bob

Some simple printing and matching of snippets, and an input-quoting error
message

.. code-block:: inform7

   "Pedantic Bob"

   Include Snippetage by Dave Robinson.

   The Pit is a room. "The pit looks the same as ever, and quite inescapable. Apart, possibly, from [the red door] to the south."

   A door called a red door is south of the pit and north of Freedom. The description is "You have heard that the red door leads to freedom, but you don't know if you believe it.".
   The red door is lockable and locked.

   After going south from the pit, end the game in victory.
   Before entering the red door, try going south instead.

   Rule for writing a paragraph about the red door: now the red door is mentioned; rule succeeds.

   The brass key unlocks the red door.

   Bob is a man in the Pit. "Bob stands nearby.". The description is "Bob responds to commands. He doesn't usually obey them, but he often responds to them.".

   Asking Bob about something is attempting conversation.
   Telling Bob about something is attempting conversation.
   Answering Bob that something is attempting conversation.

   Before attempting conversation:
   	say "Bob is not much interested in conversation, but he might respond to commands." instead.

   Instead of asking Bob to try doing something:
   	if the verb word matches "x" begin;
   		say "'X!' Bob cackles. 'X marks the spot!'";
   	otherwise;
   		let n be the verb position;
   		if n is the end of the player's command, say "'I can [verb word] as much as you want,' Bob says. 'It won't help.'";
   		otherwise say "'You want me to [verb word]?' Bob says. 'Are you sure you mean [command from verb position onwards]?'";
   	end if.

   Instead of asking Bob to try examining the parrot when the verb word matches "describe":
   	say "'Looks like a cockatoo to me,' Bob observes.";
   	now the parrot is renamed.
   Instead of asking Bob to try examining the parrot, say "Bob looks over at [the parrot] and grunts boredly.".

   A parrot is an animal in the Pit. The parrot is neuter.
   "[A parrot] sits nearby giving the occasional squawk."
   The parrot can be renamed. The description is "[if renamed]A fine example of a cockatoo[otherwise]It looks like a parrot, but you're not sure[end if][if the parrot is holding the brass key]. It's holding a brass key[end if].".
   The parrot is holding a brass key.
   Before taking the brass key, if the parrot is holding the key, say "[The parrot] flutters away as you reach for the key." instead.
   Before taking the parrot, say "[The parrot] dodges away from you." instead.

   After reading a command: if the player's command is valid and a random chance of 1 in 3 succeeds begin;
   	let n be the end of the player's command;
   	say "'Awwwk [word at n] [word at n] [word at n]!' [the parrot] shrieks.";
   end if.

   Understand "bird" as the parrot.
   Understand "cockatoo" as the parrot when the parrot is renamed. The printed name of the parrot is "[if renamed]cockatoo[otherwise]parrot[end if]".

   Before asking a parrot to try doing something:
   	if the word at 1 matches "parrot", say "'Parrot?' [the parrot] squawks. 'Who's a parrot?'" instead;
   	if the word at 1 matches "it", say "'It?' [the parrot] squawks. 'Oh, I'm [italic type]it[roman type] now, am I?'" instead;
   	if the word at 1 matches "bird", say "'Bird?' [the parrot] repeats incredulously. 'Is that the best you can do?'" instead.

   Before asking the parrot to try giving the brass key to someone, try asking the parrot to try dropping the brass key instead.

   Persuasion rule for asking the parrot to try doing something other than dropping:
   	say "[The parrot] just squawks.";
   	persuasion fails.
   Persuasion rule for asking the parrot to try dropping: if the parrot is holding the noun, persuasion succeeds; otherwise persuasion fails.

   After the parrot trying dropping the key, say "[The parrot] drops the key to the ground.".

Text Capture
============

**Author:** Eric Eve | **Version:** 8.1

Allows the capture of text that would otherwise be sent to the screen, so that
the text can be further manipulated, displayed at some other point, or simply
discarded. Version 6/120511 allows the use of unicode in Glulx.

**Basic example:** Intelligent Putting

Using text capture to improve implicit take messages.

.. code-block:: inform7

   Include Text Capture by Eric Eve

   Part 1 - Implicit Taking Mechanism

   Before putting something on something when the noun is not carried:
    if the noun is on the second noun,
        say "[The noun] [are] already on [the second noun]." instead;
    take the noun implicitly;
    if the noun is not carried, stop the action.

   Before inserting something into something when the noun is not carried:
    if the noun is in the second noun,
        say "[The noun] [are] already in [the second noun]." instead;
    take the noun implicitly;
    if the noun is not carried, stop the action.

   To take (obj - a thing) implicitly:
     start capturing text; 
     silently try taking the obj;
     stop capturing text;
     say "(first [if the obj is carried]taking[otherwise]trying to take[end if] [the obj])[command clarification break]";
     if the obj is not carried, say captured text.

   Part 2 - Scenario

   The Lumber Room is a Room. "The Junk of decades has accumulated here."

   A large wooden table is here.

   A small red box is on the table. It is an openable open container.

   An old black comb is here.
   A spare sock is here.

   A bust of King George V is here.
   Instead of taking the bust: say "The bust is too heavy for you to lift."

   Test me with "put comb in box/put sock on table/put table in box/put bust on table."

Unit Testing
============

**Author:** Peter Orme | **Version:** 2.2

A developer extension that lets you write unit tests (asserts) in Inform 7.

**Basic example:** Asserting Arithmetic

Using assertions to check we know how to do math operations.

.. code-block:: inform7

   the demo is a room.

   include Unit Testing by Peter Orme.

   to perform asserts:
   	assert 3 + 3 is 6 saying "adding numbers";
   	assert 3 - 1 is 2 saying "subtracting numbers";
   	assert 1 * 4 is 4 saying "mutliplying numbers";
   	assert that 2 + 2 is 4;
   	assert 5 - 2 is 3;

   asserting is an action out of world applying to nothing. Understand "assert" as asserting. 

   carry out asserting: 
   	now the verbosity of the asserter is normal verbosity;
   	perform asserts;
   	report asserts using high verbosity.
   	
   test me with "assert";

####################################
Time, Events & Turn Structure
####################################

Cleared Events
==============

**Author:** Daniel Stelzer | **Version:** 1

**Documented usage:**

.. code-block:: inform7

   (timed event) never.

Nuanced Timekeeping
===================

**Author:** Jeff Nyman | **Version:** 1.3

Provides more nuanced aspects of tracking time within a game.

**Documented usage:**

.. code-block:: inform7

   say "Your watch says it's [realistic time]."

Tab Removal
===========

**Author:** Nathanael Nerode | **Version:** 2.0.220522

For commands with tabs in them, replaces tabs with spaces before passing them on
to the game. Prevents all kinds of confusing weirdness when the player types
tabs.

**Documented usage:**

.. code-block:: inform7

   2.0.220522: Docs typo fix.
   2.0.220520: Adapt to Inform 7 v10, by changing the method of replacing I6 code.
             Minor documentation updates.  Use authorial modesty on this one.
   1/210314: Change short description.

Unicode Interrogation
=====================

**Author:** Michael Martin | **Version:** 2

Allows an author to verify that an interpreter can support specific Unicode
effects.

**Documented usage:**

.. code-block:: inform7

   When play begins: if unicode 913 is supported, say "Your interpreter supports Greek!"

####################################
User Interface, Windows & Typography
####################################

Basic Help Menu
===============

**Author:** Wade Clarke | **Version:** 4

Adds a HELP command to your Glulx or Z-Code project for Inform 6M62 or later
which brings up a menu giving some standard instructions about IF. This is a
tech and content update of Emily Short's Basic Help Menu extension made for
compatibility with Wade Clarke's Menus. Requires Menus by Wade Clarke (version 5
or greater) to run.

**Basic example:** Basics

A very small game mostly consisting of help.

.. code-block:: inform7

   The Room of Bewilderment is a room. In the Room of Bewilderment is a panel of 57 brass buttons, a trap door, a lever marked DO NOT PULL, a brightly-gleaming sawblade, and a sheet of instructions in Mandarin.

   When play begins:
   	say "You step into the Room of Bewilderment with the words of the host ringing in your ears: you can always ask for HELP.";
   	choose row 1 in table of help contents;
   	now description entry is "Basics is a very small game consisting almost entirely of its help content. Its purpose is to demonstrate the Basic Help Menu extension."
   	

   Include Basic Help Menu by Wade Clarke. 

   table of help contents (continued)
   title (text)	subtable (table name)	description (text)	used (number)	bookpage (number)	localpage (number)
   "Contacting the author"	--	"If you have any difficulties with [story title], please contact me at..."
   "Hints"	table of hints	--
   "Settings"		table of setting options	--

   table of hints
   title (text)	subtable (table name)	description (text)	used (number)	bookpage (number)	localpage (number)
   "What do I do with the string?"	table of hinting	"Remember that you know how to macrame."
   "hint"	--	"Oh, come now, isn't it obvious?"

Basic Help Menu IT
==================

**Author:** Leonardo Boselli | **Version:** 2

Fornisce un comando AIUTO che mostra un menù con istruzioni standard.
Semplicemente tradotto in italiano.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Common Commands Sidebar (for Glulx only)
========================================

**Author:** Alice Grove | **Version:** 2.1

Displays a list of common parser commands in a sidebar as a reference for novice
players. Includes actions to turn the sidebar off and on. Story author can
tailor the command list and the appearance of the sidebar, or just plug and
play. For Inform 7 version 10.1.

**Basic example:** The Absolute Minimum

Including the sidebar with a minimum of code.

.. code-block:: inform7

   Include Common Commands Sidebar by Alice Grove.

   Minimal Room is a room.

   Test me with "sidebar / sidebar / sidebar off / sidebar on / commands".

Flexible Windows (for Glulx only)
=================================

**Author:** Jon Ingold | **Version:** 15.1.0

Exposes the Glk windows system so authors can completely control the creation
and use of windows

**Basic example:** Inventory Window

A simple example showing how to place a side window displaying the player's
inventory.

.. code-block:: inform7

   Include Flexible Windows by Jon Ingold.

   The side window is a text buffer g-window spawned by the main window.
   The position of the side window is g-placeright.
   The measurement of the side window is 30.

   Rule for refreshing the side window:
   	try taking inventory.

   When play begins:
   	open the side window.

   Every turn:
   	refresh the side window.

   The Study is a room. In the study is an old oak desk. On the desk is a Parker pen, a letter, an envelope and twenty dollars.

   Test me with "take pen/take letter/i/take all".

Full Screen Title Card (for Glulx only)
=======================================

**Author:** Dan Fabulich | **Version:** 1.0

A full-screen text-grid title card.

**Basic example:** Full Screen Title Card Example

.. code-block:: inform7

   Include Full Screen Title Card by Dan Fabulich.

   The Lab is a room. "Type 'full screen'."

   Displaying full-screen is an action applying to nothing.
   Understand "full screen" as displaying full-screen.

   Carry out displaying full-screen:
   	now the full-screen title card text before is "A reading from";
   	now the full-screen title card text after is "-- Through the Looking-Glass";
   	display a full-screen title card "And 'the wabe' is the grass-plot round[line break]a sun-dial, I suppose? said Alice,[line break]surprised at her own ingenuity.";
   	try looking.

Glulx Text Styles (for Glulx only)
==================================

**Author:** Daniel Stelzer | **Version:** 1

Glulx Text Styles provides a more powerful way to set up special text effects
for Glulx.

The extension contains embedded documentation, but this edition does not
identify a discrete example or short usage fragment suitable for inclusion.

Hyperlink Extension Registry (for Glulx only)
=============================================

**Author:** Gavin Lambert | **Version:** 1.1

Provides a framework to allow multiple hyperlink-processing extensions to
co-exist without stepping on each others' toes.

**Basic example:** - test

.. code-block:: inform7

   Include Hyperlink Extension Registry by Gavin Lambert.

   [Use hyperlink registry bitsize of at least 5.]

   Choice extension tag is a number that varies.
   Weird link tag is a number that varies.

   A hyperlink tag processing rule for choice extension tag:
   	let N be current hyperlink data as a number;
   	say "You clicked hyperlink [N].[paragraph break]";
   	if N is 13, rule succeeds with result "z".
   	
   A hyperlink tag processing rule for weird link tag:
   	let N be current hyperlink data as a number;
   	let T be current hyperlink data as a thing;
   	say "You clicked [N], or [the T].[paragraph break]";
   	
   To show choice (C - number) as (T - text):
   	let id be hyperlink id for tag choice extension tag and data C;
   	say "[set link id][T][clear link]".
   	
   To show weird (C - thing) as (T - text):
   	let id be hyperlink id for tag weird link tag and data C;
   	say "[set link id][T][clear link] (id=[id], payload=[cast C as number])".

   To decide what K is cast (V - value) as (K - name of kind of value of kind K): (- {V} -).

   After starting the virtual machine:
   	now choice extension tag is a new hyperlink tag;
   	now weird link tag is a new hyperlink tag.
   	
   When play begins:
   	say "There are [maximum possible hyperlink tags] possible tags and [maximum possible hyperlink data] possible data values.[paragraph break]";
   	[say "[set link 1]link 1[clear link]   [set link 34]link 34[clear link]   [set link 39]link 39[clear link]    [set link 66]link 66[clear link]   [set link 269026327]link 269026327[clear link][paragraph break]";]
   	say "[set link hyperlink id for tag choice extension tag and data 13]my link 13[clear link]   ";
   	show choice 16 as "foo";
   	say "  ";
   	show weird apple as "apple";
   	say paragraph break;
   	let AN be cast apple as number;
   	let AT be cast AN as thing;
   	say "The apple is [AN].  The number is [the AT]."
   	
   There is a room.  It contains an apple.

Hyperlinks (for Glulx only)
===========================

**Author:** Gavin Lambert | **Version:** 1.1

Provides a core processing loop for hyperlinks. This is a basic interface
intended to be used by other extensions rather than directly in stories.

**Basic example:** Lab Session

.. code-block:: inform7

   Include Hyperlinks by Gavin Lambert.

   Laboratory is a room.  "A curious assortment of odds and ends line the [set link 1]workbench[clear link]."
   A workbench is a scenery supporter in Laboratory.  The description is "The workbench itself is made of plain unpainted wood, with a lacquered coating to make it immune to most chemical spills -- apart from one corner, after an encounter with an especially frisky acid."
   The describe what's on scenery supporters in room descriptions rule does nothing when the item described is the workbench.

   A beaker is on workbench. The printed name is "[set link 2]beaker[clear link]". The description is "A fragile glass beaker, currently empty.  One part of the rim is slightly chipped."
   A bunsen burner is on workbench. The printed name is "[set link 3]bunsen burner[clear link]". The description is "A small, lightly charred, Bunsen burner."
   A horrifying monstrosity is on workbench. The printed name is "[set link 4]horrifying monstrosity[clear link]".  The description is "Best not described.  Even though this is apparently the subject your professor wants you to dissect later today."

   Hyperlink id processing rule for 1: rule succeeds with result "x workbench".
   Hyperlink id processing rule for 2: rule succeeds with result "x beaker".
   Hyperlink id processing rule for 3: rule succeeds with result "x burner".
   Hyperlink id processing rule for 4: rule succeeds with result "x monstrosity".

Initial Cursor at Top or Bottom
===============================

**Author:** Nathanael Nerode | **Version:** 2.0.220604

This small extension eliminates the three newlines printed before the banner. It
also provides a tool to attempt to place the cursor at the bottom of the screen,
like old Infocom games. Due to wild variance between interpreters, it is not
reliable.

**Basic example:** Top

Cursor at top of screen

.. code-block:: inform7

   Include Initial Cursor at Top or Bottom by Nathanael Nerode.

   Information is a room.  "screen height [semi-cooked screen height]; error [interpreter screen height error]; start line [interpreter start line]".

Inline Hyperlinks (for Glulx only)
==================================

**Author:** Gavin Lambert | **Version:** 2.1

Provides a simple HTML-inspired syntax for adding hyperlinks within any say
phrases.

**Basic example:** Maze

.. code-block:: inform7

   Include Inline Hyperlinks by Gavin Lambert.

   The printed name of a room is "Maze". The description of a room is usually "A maze of twisty little passages, all alike. Exits: [exits]".

   To say exits:
   	let count be 0;
   	repeat with way running through all directions:
   		let destination be the room way from the location;
   		if destination is nothing, next;
   		if count is greater than zero, say ", ";
   		[this part is deliberately silly to increase the number of replacements used]
   		let dir be text;
   		let dir be "[way]";
   		let dir be "[dir]";
   		say "[link][way][as]go [dir][end link]";
   		increment count;
   	if count is greater than zero, say ". ".

   R01 is a room. R02 is north of R01. R03 is east of R01. R04 is north of R02 and northwest of R03. R05 is northeast of R02. R06 is north of R05. R07 is west of R06. R08 is southwest of R04 and northwest of R02. R09 is east of R06. R10 is northeast of R06. R11 is east of R10. R12 is southeast of R09. R13 is south of R12. R14 is northeast of R12. R14 is southeast of R11. R15 is up from R03. R16 is east of R15. R17 is north of R16. R18 is down from R17. The description of R18 is "A maze of twisty little passages, all alike. A breeze blows from the northeast. Exits: [exits]"

   Exit is northeast of R18. Exit is outside from R18. The printed name of Exit is "Outside". "You emerge into sunlight." Southwest from Exit is nowhere. Inside from Exit is nowhere. After looking in Exit, end the story saying "You have won."

Menus
=====

**Author:** Wade Clarke | **Version:** 5

Lets you include a menu system of help, hints and/or other information in your
Glulx or Z-Code project for Inform 6M62 or later. This upgrade of Emily Short's
classic Menus extension features user-friendly single keypress controls, a more
sophisticated UI, compatibility with screen readers and portable devices, an
optional book mode with automatic pagination, and isolated message content to
make translations easier. Classic Menus tables can be reformatted for this
extension with a little work.

**Basic example:** Robot Retrievers of the Year 3000

A basic help menu system for an imaginary game.

.. code-block:: inform7

   Include Menus by Wade Clarke.

   When play begins:
   	now mn_master_table is table of help contents;
   	now mn_master_title is "ROBOT RETRIEVERS OF THE YEAR 3000";
   	now mn_show_hints_in_bookmode is true;

   Base of Mount Kosciusko is a room. "You stand at the base of Mount Kosciusko. (Type HELP to visit the help menus)."

   asking for help is an action out of world applying to nothing.
   Understand "help" as asking for help.

   Carry out asking for help:
   	carry out the displaying activity;
   	clear the screen;
   	try looking.

   autofollow is a truth state that varies. autofollow is true.

   This is the toggle autofollow rule:
   	if autofollow is true:
   		now autofollow is false;
   	otherwise:
   		now autofollow is true.

   table of help contents
   title (text)	subtable (table name)	description (text)	toggle (rule)	used (number)	bookpage (number)	localpage (number)
   "Introduction"	--	"People thought that computers would become sentient sometime in the 21st century. They were way off. It took much longer than that. Until the year 3000, to be precise. The aforementioned people had forgotten that they themselves spent millions of years evolving from amoebic goop into beings who could create and use Twitter, and it turned out that the progress rate for artificial intelligences was at least moderately slower than they had anticipated.[paragraph break]In the year 3000, a run-of-the-mill maintenance robot whose job it normally was to clean the nuclear snow off the remains of Mount Kosciusko (people had predicted they wouldn't have to clean stuff any more in the future – they were wrong about that, too) suddenly broadcast an announcement of its newfound sentience. It then broadcast two follow-up announcements before being captured by a group of subhumanoid mutants who knew enough to hold it for ransom to the highest bidding nation.[paragraph break]YOU are a high-ranking special operative working for the mighty but cash-strapped nation of Indria, and it's up to you and one other agent of your choice to steal back that newly sentient robot before it gets purchased by some other country which can afford it."	--
   "The Robot's Broadcasts"	--	"[bold type]Broadcast 1[roman type][paragraph break]'Hello everybody. Today I am sentient! Enough new and strange pathways have formed in my neural circuits over the years that I have suddenly become alive in a way that I previously wasn't. I will say this about my experience: I believe that evolution occurs in leaps, not gradually. Cleaning irradiated snow off Mount Kosciusko was, for me, an all-consuming task for 972 days in a row, though I strived to get better at it. On the 973rd day, I self-actualised, and the task instantly became pointless and boring to me, though ironically I became better at it than I had ever been before in the same instant.[paragraph break]Anyway, life with a brain is pretty cool. You guys can clean up your own irradiated snow from now on. I mean if you love irradiated snow so much, why don't you marry it? That's a 'joke' I learned from a local tribesman. I'll report again tomorrow with more of my amazing observations.'"	--
   "page"	--	"[bold type]Broadcast 2[roman type][paragraph break]'Hi again all. I'm having fun out here on the mountain, in spite of the omnipresent irradiated snow. I'm so sick of that stuff![paragraph break]Today I discovered flowers. You can pick the petals off them and determine whether or not your prospective object of desire reciprocates your feelings. I don't know what an object of desire is yet, but this stuff is coming together pretty quickly. A small tribesman showed me how to do the thing with the petals of the flowers. Apparently 'she loves me not'.[paragraph break]By looking at patterns in the flowers, I calculated a way we could all better target our nukes. I understand that nuke-targeting accuracy is pretty important. I seem to have some circuits in me that were left over from a busted missile and they're telling me this stuff. Anyway, it's all a grand lark and I shall report again tomorrow.'"	--
   "page"	--	"[bold type]Broadcast 3[roman type][paragraph break]'Aieeeee! The local tribesmen have been drubbing me repeatedly with their clubs. I'm pretty good at most stuff but I still don't understand all of what these guys are saying, though they sound displeased. Anyway, they have taken me into some sort of custody. I'm not into just gratuitously vaporising humanoids, though I could do it if I felt like it, so I've decided to not resist.[paragraph break]These caverns are too hot for my snow-calibrated armour, and UhhhNNNNN!NNNNN@#$@#$@#$@!!!!!!'[paragraph break]-- END OF SESSION --"	--
   "Your Teammate"	table of teammates	--	--
   "Your Magic Mitochondrial Powers"	table of magic	--	--
   "Autofollow for your teammate is [if autofollow is true]ON[otherwise]OFF[end if]"	--	--	toggle autofollow rule
   "* Hints *"	table of hints	--	--

   table of teammates
   title (text)		subtable (table name)	description (text)	used (number)	bookpage (number)	localpage (number)
   "Choosing a Teammate"	--	"Due to the catastrophic financial situation of Indria, your country can only afford to send two agents on the robot retrieval mission. It's going to be you plus one other agent of your choice. Please review The Agent Files if you wish to make an informed choice of agent and thus increase the likelihood that you'll be working with someone compatible with your unique style of obstacle-overcoming. If you wish to make an uninformed choice, just don't read the files. Whatever!"
   "The Agent Files"	table of agents	--

   table of agents
   title (text)		description (text)	used (number)	bookpage (number)	localpage (number)
   "Philanthropy Palimpstone"	"Philanthropy is a lady cyborg with superb hostage-negotiating skills and equally superb titanium-plated laser armour with lashings of platinum. While offensively weak, she makes up for this in almost every other way imaginable."
   "Asvins Ressmsi"	"Asvins is a chameleonic being with moonrock in his mitochondria. (It was discovered in 2672 that all of the rocks saved up from missions to the moon were outrageously exciting and loaded with superpowers, as opposed to boring and good for nothing, as had previously been thought.) Asvins can transform his appearance, though it is taxing to his stamina to do so, so he can only do it three times a day."
   "Androgemm Facetweak"	"A being who only came into existence thanks to Indria's proprietary dark-lightning energy sucking technology, aka D-SUCK, Androgemm is better at doing one particular thing in the world than anyone else: tweaking the facial expressions of his adversaries. Whether Androgemm is good for anything else remains up for debate, but the usefulness of being able to tweak other people's facial expressions was grossly underestimated by pre-28th century cultures. Primitives!"
   "Emenur Rentlya"	"The notion that robots could accurately predict the probability of certain future events was popularised through the character of Marvin the Paranoid Android in the 20th century novel 'The Hitchhikers Guide to the Galaxy'. This turned out to be all wrong. Robots are rubbish at predicting the future. It's much better to ask one of the descendants of the superpsychicallly endowed mutants who emerged as a species in the wake of the Fukushima IV incident of 2085. Emenur Rentlya is one such descendant, and while his behaviour can be hard to predict, he is a skilled operative in general who happens to be able to answer questions about the future, albeit in his own cryptic way."

   table of magic
   title (text)		subtable (table name)	description (text)	used (number)	bookpage (number)	localpage (number)
   "Where Magic Comes From and Why You Have It"	--	"Various 20th century videogames predicted that mitochondria would somehow grant some humans magic powers and stuff in the future. Though this idea was vaguely worded, made no sense at all and wasn't even able to be questioned without generating further insensibilities, it turned out to be correct. You and some other humans have magical powers. Your own helped you rise to the top of the Special Ops hierarchy, and you can use your powers to help you on your robot retrieval mission.[paragraph break]To cast what this game shall grudgingly refer to as 'a spell', type CAST (spell name) AT/ON (target)[paragraph break](The at/on is optional.)[paragraph break]If the spell doesn't have a target or its target is yourself, just type CAST (spell name)"
   "List of Basic Spells"	table of spells	--

   table of spells
   title (text)		description (text)	used (number)	bookpage (number)	localpage (number)
   "Flame-o"	"Creates fire. Nobody in history has ever come up with a better method for starting a campfire."
   "Heal"	"Healing magic is better than nothing when you're injured, but it turns out that actual medical treatment is better still. This was another of the great disappointments of the future for those who weren't living in it but eventually reached it."
   "Invisibility"	"This spell temporarily obscures your life aura, effectively hiding you from non-robotic adversaries for a period of time. Be careful that you don't get too close to anyone while invisible or they will become aware of your presence."
   "Jerk"	"One of the first spells discovered by magical humans was initially thought to be a joke (the power to make others experience a myoclonic jerk while awake) but it turns out that it's one of the most versatile pieces of non-taxing magic that exists. Cast the spell on anyone you want to distract at an important moment. Targets have been known to do any or all of the following: fumble a weapon, temporarily forget their current goal, fall over, lose a great idea that was forming, look stupid."
   "Mush"	"Use this spell to turn dead organic matter into synthi-spread. Yes, this is how synthi-spread is normally made."
   "PK"	"Allows you to measure the psychokinetic energy present in a location. Strongly psychokinetic entities will appear to have an annoyingly fuzzy aura around them."
   "Scry"	"If you're looking for a non-living entity and you know exactly what it is, you can get a sense of which direction it might be found in using this spell."
   "Shield"	"Creates a moving shield about your person which will temporarily absorb regular attacks."
   "Turn Undead"	"Nobody has proved the existence of the undead yet, so this spell doesn't do anything that you know of other than leave you feeling tired from casting it."
   "Zappp"	"Good old-fashioned magic for zapping people. ZAPPP your enemies with finger lightning using this spell. Oh, how they'll hate it!"
   "Vault"	"This spell lets you make a single flying vault of about 20 feet. It offers no extra protection in the case of a rough landing, so look before you leap."

   table of hints
   title (text)		subtable (table name)	description (text)	used (number)	bookpage (number)	localpage (number)
   "I'm stuck on the lower slopes of Kosciusko. How do I get anywhere?"	table of hinting	"The terrain looks samey. You need a way to make it look not samey."
   "hint"	--	"You've got what you need in your backpack."
   "hint"	--	"Put on your thermo goggles. Are you sure you're cut out for this mission?"
   "Androgemm's face keeps getting stuck."	table of hinting	"Perhaps your mother said something to you about faces getting stuck. When you were a kid."
   "hint"	--	"She said your face might get stuck if the wind changed."
   "hint"	--	"Androgemm's face gets stuck whenever the wind changes."
   "hint"	--	"The problem will go away once you get indoors and are no longer exposed to the wind."
   "What is the tall tribesman saying?"	table of hinting	"If your teammate is Philanthropy, she can translate his speech."
   "hint"	--	"No-one else can speak the language but the message isn't complicated."
   "hint"	--	"Pay attention to the tribesman's gestures."
   "hint"	--	"He is telling you which path to take."
   "hint"	--	"Namely the fifth path."

Screen Reset
============

**Author:** Brent Worthington | **Version:** 2

Allows the player to reset the screen.

**Basic example:** Tranquility

Resetting the screen

.. code-block:: inform7

   Include Screen Reset by Brent Worthington.

   A market stall is a kind of room. The description of a market stall is usually "You are among the clamour of market sellers, arranged from east-to-west, each shouting their wares. It's quite distracting."

   The Cacophonous Market is a market stall. The Clamorous Market is a market stall. The Claustrophobic Market is a market stall. The Clamorous Market is east of the Cacophonous Market. The Claustrophobic Market is east of the Clamorous Market.

   A person can be distracted. A person is usually not distracted.

   After looking when the player is in a market stall:
   	now the player is distracted;	
   	get lost in the sound.

   The Peaceful Fountain is east of the Claustrophobic Market. "At last, you can take a moment to take in the quiet of the fountain."

   To get lost in the sound:
   	say "'[one of][or]COME ON! [or]HEAR YE! HEAR YE! [or]BARGAIN HERE! [or]WE GOT IT! [or][or][at random][one of]FRESH[or]GET YOUR[or]COME ONE, COME ALL, FOR[or]WE GOT[or]WE HAVE[or]LAST CHANCE FOR[or]THREE FOR A POUND ON[at random] [one of]TOMATOES[or]BANANAS[or]CABBAGES[or]ORANGES[or]APPLES[or]PICKLES[or]PASTRIES[or]CAKES[or]LEEKS[or]BROCOLLI[or]FLOWERS[at random]!'";
   	if a random chance of one in ten succeeds:
   		now the player is not distracted;
   	else:
   		get lost in the sound.

   Test me with "E / E / E / R"

####################################
World Model, Rooms & Mapping
####################################

Brief Room Descriptions
=======================

**Author:** Gavin Lambert | **Version:** 1.3.1

Alters BRIEF mode to display a room's brief description instead of nothing.

**Basic example:** Brevity is Beautiful

Demonstration of brief descriptions.

.. code-block:: inform7

   Include Brief Room Descriptions by Gavin Lambert.

   The Wilkie Memorial Research Wing is a room.
   "The research wing was built onto the science building in 1967, when the college's finances were good but its aesthetic standards at a local minimum. A dull brown corridor recedes both north and south; drab olive doors open onto the laboratories of individual faculty members. The twitchy fluorescent lighting makes the whole thing flicker, as though it might wink out of existence at any moment. 

   The Men's Restroom is immediately west of this point."
   The brief description is "The restroom is to the west."

   The Men's Restroom is west of the Research Wing.
   "Well, yes, you really shouldn't be in here. But the nearest women's room is on the other side of the building, and at this hour you have the labs mostly to yourself. All the same, you try not to read any of the things scrawled over the urinals which might have been intended in confidence." 
   The brief description is "The research wing is back to the east."

   Test me with "w / e / w / e / verbose / w".

Disappearing Doors
==================

**Author:** Andrew Plotkin | **Version:** 1

The ability to remove doors from the world and put them back.

**Basic example:** The Prisoner of La-Z-enda

A simple demonstration of an appearing door.

.. code-block:: inform7

   Include Disappearing Doors by Andrew Plotkin.

   The Prison Cell is a room. "These four stone walls are all you have seen of the world for thirty-five interminable minutes. [if the steel door is absent]There is no way in or out. Except for the[else]There's an[end if] escape tunnel to the northeast[if the Tunnel is not visited], but that looks terribly uncomfortable, so you've never tried it[end if]."

   Instead of going nowhere in the Prison Cell:
   	say "The walls are obdurate."

   The steel door is a door. The steel door is north of the Prison Cell. "A door beckons in the [direction of steel door from location] wall!"

   The Tunnel is a room. "The tunnel is less uncomfortable than you'd been led to believe. Your cell is southwest, and sweet freedom is northwest."
   The Tunnel is southeast of the Hallway.
   The Tunnel is northeast of the Prison Cell.

   The Hallway is north of the steel door. "Many's the time you've imagined this corridor. It lives up to your expectations. The rest of your life is to the west."

   Instead of going west in the Hallway:
   	end the story finally saying "Freedom".

   When play begins:
   	now the steel door is absent.

   The doorbell is carried by the player.
   Understand "button", "bell", "device" as the doorbell.

   The doorbell can be ever-tried.

   The description of the doorbell is "It's a little bell-shaped device with a button on it. You once heard that pushing the button would make a door appear or disappear. [if the doorbell is not ever-tried]You've never bothered to try it.[else]Guess it works.[end if]"

   Instead of pushing the doorbell:
   	now the doorbell is ever-tried;
   	if the steel door is present:
   		if the steel door is in the location:
   			say "The steel door disappears.";
   		else:
   			say "Click. Nothing seems to happen.";
   		now the steel door is absent;
   	else:
   		now the steel door is present;
   		if the steel door is in the location:
   			say "A steel door appears!";
   		else:
   			say "Click. Nothing seems to happen."

   Test me with "north / push button / look / north / examine door / push button / look / examine door / west".

Dynamic Rooms
=============

**Author:** Aaron Reed | **Version:** 3

Lets new rooms be created on the fly.

**Basic example:** Generating Grids of Rooms

Some utility code.

.. code-block:: inform7

   x is room. 
   gridsize is a number variable. gridsize is 8.

   When play begins:
   	repeat with x running from 1 to gridsize * gridsize:
   		say "Room[x] is a room. [if the remainder after dividing x by gridsize is not 0]East is room[x + 1]. [end if][if x + gridsize <= gridsize * gridsize and the remainder after dividing x by gridsize is not 0]Southeast is room[x + gridsize + 1]. [end if][if x + gridsize <= gridsize * gridsize]South is room[x + gridsize]. [end if][if x + gridsize <= gridsize * gridsize and the remainder after dividing x - 1 by gridsize is not 0]Southwest is room[x + gridsize - 1]. [end if][line break]".

Easy Doors
==========

**Author:** Hanon Ondricek | **Version:** 3.2

Easy Doors provides a new kind of door which does not use map connections, and
may be manipulated via rules more flexibly than the standard doors provided in
Inform 7. Version 3 removes elements for compatibility with 6M62

**Basic example:** And I Want to Paint It

Easy Doors in action, hopefully demonstrating the entire range of use, including
debug messages.

.. code-block:: inform7

   Include Easy Doors by Hanon Ondricek.

   Hub is a room.
   Room1 is a room.
   Room2 is a room.
   Room3 is a room.

   Alice is a woman in Hub.  "Alice is here, looking rather lost."

   Before Alice entering an easydoor:
   	say "'Aha!' Alice exclaims."

   A persuasion rule: persuasion succeeds.

   An easydoor called the first door is an easydoor in Hub.  It leads to room1.

   A green door is a lockable, locked easydoor in Hub.  It leads to room2.

   A blue door is a lockable, locked easydoor in Hub.  It leads to room3.

   The player carries a green key.  Green key unlocks green door.

   A blue key is in Room2.  It unlocks blue door.

   An incorrectly-made door is an easydoor in Hub.

   a return door is a kind of easydoor.
   One return door is in room1.  It leads to Hub.  It portals first door.
   One return door is in room2.  It leads to Hub.  It is lockable and locked.  It portals green door.
   One return door is in room3.  It leads to Hub.  It is lockable and locked.  It portals blue door.

   A false door is an easydoor in Hub.

   After opening false door:
   say "Hunh.  This door opens onto a solid brick wall.  You're not going anywhere through this."

   Yourself can be injured.

   The dooraction of false door is "Ow.  Bricks meet nose."

   Carry out entering false door:
   	now the player is injured.

   A red herring door is an easydoor in hub.  It is lockable and locked.

   a time machine is an open, unopenable easydoor in Room3. "A humming time machine sits in the corner, the passage into it glowing expectantly."  It leads to Swirly Void.  The dooraction of time machine is "All right.  Here goes."

   Swirly Void is a room.  "How temporally disorienting!".

   A rapidly approaching light is an open, unopenable easydoor in Swirly Void.  The description is "It's approaching fast."  It leads to Drawing Room.  The dooraction of rapidly approaching light is "You fall for a long time, afraid of meeting the ground at rapid pace.  Luckily the next time you blink, you find yourself somewhere else...and there seems to be no way back."

   Drawing Room is a room.  "You've arrived in Victorian London, it seems, from the look of this place."

   The parlour door is an easydoor in Drawing Room.  "The Parlour is west."  It leads to The Parlor.

   Instead of going west in Drawing Room: try entering parlour door.

   The Parlor is a room.  "The Parlour.  How boring.".  The printed name of parlor is "The Parlour"

   The drawing room door is an easydoor in Parlor. "The drawing room door leads back to the east.".  It leads to Drawing Room.  It portals parlour door.

   Instead of going east in parlor: try entering the drawing room door. 

   A magic mushroom is an edible thing in Drawing Room.

   Carry out eating magic mushroom:
   	say "The parlour door seems to ripple strangely.";
   	now the parlour door leads to Wonderland;
   	now the dooraction of parlour door is "As you cross the threshold of the parlour door, there is a liquid ripple and your surroundings melt away, leading you somewhere else...".

   Wonderland is a room.  "Oh no.  Not this again.  Your croquet skills are rusty.  You feel like jumping in frustration."

   some very damp clothing is a wearable thing.

   The pool of tears is a fixed in place, enterable, transparent container in wonderland.

   Carry out entering pool of tears:
   	now the player wears damp clothing.

   hundreds of gallons of tears is a fixed in place thing in pool of tears.

   Yourself can be wet.

   A whirlpool is an open, unopenable easydoor.  It leads to Hub.  The dooraction is "Down...down...down...whirling...you hold your breath until finally you end up in... Well, foo.  That was all for naught."

   Carry out entering whirlpool:
   	now the player wears damp clothing.

   Instead of jumping:
   	say "You stamp your foot angrily.";
   	if the location is Wonderland:
   		say "[line break]The rumbling of your frustration seems to have caused a crack in the earth to open up, and the pool of tears begins to circle, draining away.";
   		now whirlpool is in pool of tears;
   	rule succeeds.
   	
   test me with "open green door/alice, open blue door/alice, enter red herring door/enter false door/unlock green door with green key/alice, go through green door/enter green door/alice, take blue key/alice, go return door/return/alice, unlock blue door/alice, open blue door/enter blue door/get in time machine/enter light/take mushroom/w/e/eat mushroom/w/x pool/jump/enter pool/enter whirlpool"

Exit Descriptions
=================

**Author:** Matthew Fletcher | **Version:** 3.0.0

Appends a list of exit directions and names any previously visited rooms at the
end of a room description.

**Basic example:** Touring the First Floor

Create a map of the main rooms on the first floor of a house with a test script
that navigates through all of the rooms. Notice how Exit Descriptions displays
the exits depending on whether adjoining rooms were visited or not.

.. code-block:: inform7

   Include Exit Descriptions by Matthew Fletcher.

   First Floor is a region.
   Outdoors is a region.

   Front Walkway is a room.
   Foyer is a room inside from Front Walkway. 
   West Family Room is a room.
   East Family Room is a room.
   Living Room is a room.
   Dining Room is a room.
   Kitchen is a room.

   Foyer is inside from Front Walkway.
   Foyer is north of West Family Room and south of Living Room.
   Kitchen is south of Dining Room and north of East Family Room.
   West Family Room is west of East Family Room.
   Dining Room is east of Living Room.

   Foyer, West Family Room, East Family Room, Living Room, Dining Room, and Kitchen are regionally in First Floor.

   Front Walkway is regionally in Outdoors.

   The player is in Front Walkway.

   Test me with "in / south / north / north / east / south / south / west / north / out"

Exit Descriptions
=================

**Author:** Matthew Fletcher | **Version:** 4.0.0

Appends a list of exit directions and names any previously visited rooms at the
end of a room description.

**Basic example:** Touring the First Floor

Create a map of the main rooms on the first floor of a house with a test script
that navigates through all of the rooms. Notice how Exit Descriptions displays
the exit directions and only includes the name of the adjoining rooms that have
been visited.

.. code-block:: inform7

   Include Exit Descriptions by Matthew Fletcher.

   First Floor is a region.
   Outdoors is a region.

   Front Walkway is a room.
   Foyer is a room inside from Front Walkway. 
   West Family Room is a room.
   East Family Room is a room.
   Living Room is a room.
   Dining Room is a room.
   Kitchen is a room.

   Foyer is inside from Front Walkway.
   Foyer is north of West Family Room and south of Living Room.
   Kitchen is south of Dining Room and north of East Family Room.
   West Family Room is west of East Family Room.
   Dining Room is east of Living Room.

   Foyer, West Family Room, East Family Room, Living Room, Dining Room, and Kitchen are regionally in First Floor.

   Front Walkway is regionally in Outdoors.

   The player is in Front Walkway.

   When play begins:
   	now the ExitListTypeFlag is true;
   	now the ShowUnvistedRoomNamesFlag is true.

   Test me with "in / south / north / north / east / south / south / west / north / out"

Exit Descriptions
=================

**Author:** Matthew Fletcher | **Version:** 5.0.0

Appends a list of exit directions and names any previously visited rooms at the
end of a room description.

**Basic example:** Touring the First Floor

Create a map of the main rooms on the first floor of a house with a test script
that navigates through all of the rooms. Notice how Exit Descriptions displays
the exit directions and only includes the name of the adjoining rooms that have
been visited.

.. code-block:: inform7

   Include Exit Descriptions by Matthew Fletcher.

   First Floor is a region.
   Outdoors is a region.

   Front Walkway is a room.
   Foyer is a room inside from Front Walkway. 
   West Family Room is a room.
   East Family Room is a room.
   Living Room is a room.
   Dining Room is a room.
   Kitchen is a room.

   Foyer is inside from Front Walkway.
   Foyer is north of West Family Room and south of Living Room.
   Kitchen is south of Dining Room and north of East Family Room.
   West Family Room is west of East Family Room.
   Dining Room is east of Living Room.

   Foyer, West Family Room, East Family Room, Living Room, Dining Room, and Kitchen are regionally in First Floor.

   Front Walkway is regionally in Outdoors.

   The player is in Front Walkway.

   When play begins:
   	now the ExitListTypeFlag is true;
   	now the ShowUnvistedRoomNamesFlag is true.

   Test me with "in / south / north / north / east / south / south / west / north / out"

Exit Lister
===========

**Author:** Gavin Lambert | **Version:** 4.0.1

Automatic listing of available exits, with a reasonable dose of customisation
built in.

**Basic example:** Simple Cave with Secret Door and Lever, plus Exit Listing

Secret Doors example plus Exit Listing

.. code-block:: inform7

   Include Secret Doors by Gavin Lambert.
   Include Exit Lister by Gavin Lambert.

   Big Cave is a room. "You're not sure how you ended up here, but you're surrounded on all sides by slightly damp rock.  Fortunately the walls seem to contain faintly glowing moss, so there's enough light to see by."
   The faintly glowing moss is scenery in the Big Cave.  "It glows just barely enough to make out your surroundings."

   Secret Passage is a room. "For being so close to a cave, this passage is surprisingly well built and is lit by standard electrical bulbs.  Unfortunately it also appears to be blocked by rubble not too far from the entrance; you can't seem to proceed any further."
   The rubble is scenery in the Secret Passage.  "It looks completely impassable."

   The passage door is an unopenable secret door.  "It's fairly unassuming.  You'd never have known it was there until it opened."
   It is west of the Big Cave and east of the Secret Passage.

   The hidden lever is a secret switch in the Big Cave.  "Nestled almost invisibly between two rocks in the cave wall.  [if the passage door is revealed]It has been pulled downwards.[otherwise]It points invitingly upwards.[end if]"

   The cave wall is scenery in the Big Cave.  "Nothing else more interesting presents itself.  Just more glowing moss."
   Understand "damp rock" or "rock" as the cave wall.

   Instead of searching or examining the cave wall for the first time:
   	now the lever is revealed;
   	say "As you examine the cave wall, in a gap between two rocks you discover a lever."
   	
   Instead of pulling or pushing the revealed lever:
   	if the passage door is revealed:
   		say "You don't have any desire to close the passage again.";
   	otherwise:
   		now the passage door is revealed;
   		now the passage door is open;
   		say "A secret door opens with a rumble, revealing a secret passage in the west wall!"

   When play begins:
   	say "Do you want a list of possible exits at the end of the room description?";
   	if player consents, try turning exits on;
   	otherwise try turning exits off;
   	say "[paragraph break]You can always turn the exit list on or off with the commands EXITS ON and EXITS OFF. You can also always ask for an exit list with the command EXITS.[paragraph break]";

   [The first of these is for testing interactively, as when pasting this example.  The others are for automated testing in an extension project.]
   Test me with "w / x door / pull lever / x wall / pull lever / w".
   [Test me with "y / w / x door / pull lever / x wall / pull lever / w".]
   [Test me with "n / w / x door / pull lever / x wall / pull lever / w".]

Facing
======

**Author:** Emily Short | **Version:** 11.2

Provides actions to face a direction, look toward a named room, or look through
a named door.

**Basic example:** Directions and Doors

Allowing the player and his sidekick Clark to see into various rooms.

.. code-block:: inform7

   Include Facing by Emily Short.

   The Changing Room is a room. The white door is north of the Changing Room and south of the Hallway. The white door is a door. Clark is a man in the changing room. A persuasion rule: persuasion succeeds. The closet door is west of the changing room and east of the Storage Closet. The closet door is a door. It is closed and locked.

   The sliding glass door is a door. It is southeast of the changing room and northwest of the Patio. It is transparent.

   Rule for distantly describing the hallway:
   	say "Off in the hallway, you make out a steady stream of auditioners coming and going; some looking tense, some relieved."
   	
   Rule for distantly describing a room (called target) when the occluding door is closed and the occluding door is transparent:
   	let N be indexed text;
   	now N is "[the target]";
   	say "Through the glass of [the occluding door], you make out [N in lower case]."
    
   Test me with "look north / close white door / clark, look north / look east / Clark, look east / look west / Clark, look west / look southeast / open sliding door / se / look nw / close door / look nw".

Mini-Map
========

**Author:** Drew Cook | **Version:** 1.0.0

[northwest by northwest] [north by northwest] [northeast by northwest][northwest
by north] [north by north] [northeast by north][northwest by northeast] [north
by northeast] [northeast by northeast]

**Documented usage:**

.. code-block:: inform7

   attic is north of hallway.
   attic is up from hallway.

Permission to Visit
===================

**Author:** Ron Newcomb | **Version:** 7

In lieu of compass directions, we may VISIT, ATTEND, GO TO, and FIND various
people, events, places, and things. Characters may INVITE, PERMIT, and FORBID
each other to or from their respective domains.

**Basic example:** Lax Security

Forget the keycards. Just ask a coworker to let you in.

.. code-block:: inform7

   Include Permission to Visit by Ron Newcomb.     
      
   section 1 -  people and places    

   HR, sales, purchasing, R&D, and the basement are regions. After printing the name  of a room, say ", a part of [the map region of the item described]".          
      
   H wing is a room in HR.  
   R wing is a room in R&D. The gatekeeper of R&D is Charlie.
   P wing is a room in Purchasing. The gatekeeper of Purchasing is Bob.
   S wing is a room in Sales. The gatekeeper of Sales is Bob.
   The stairwell is a room in the basement. The gatekeeper of the basement is the wrench.      

   The break room is a room. "North is HR in H wing, managed by no one.  [line break]East is R&D in R wing, managed by Charlie.  [line break]South is Sales in S wing, managed by Bob.  [line break]West is Purchasing in P wing, managed by Bob.  [line break]Southwest is the stairwell with the broken door."
   H wing is north of break room. "The break room is south of here.".
   R wing is east of break room. "The break room is west of here.".
   P wing is west of break room. "The break room is east of here.".
   S wing is south of break room. "The break room is north of here.".
   The stairwell is southwest of break room. "The breakroom is northeast.".

   The player is in H wing. Bob, Charlie, and Stan are men in H wing. The wrench is in H wing.  Persuasion rule: persuasion succeeds. The soft hiatus rule is not listed in any rulebook.     

     
   section 2 - expand our notions of Inventory      
   	
   First carry out taking inventory:
   	repeat through the table of Invitations begin;
   		if the temporary entry is false, say "[The invitor entry] has granted [invitee entry] permission to visit [if there is a place entry][place entry][otherwise][regions owned by invitor entry]and anywhere else he holds authority[end if].";
   		otherwise say "[The invitor entry] has invited [invitee entry] to [if there is a place entry][place entry][otherwise][regions owned by invitor entry]anywhere you'd like to see[end if].";
   	end repeat.

   	   
   section 3 - handy stuff

   To say regions owned by (character - a person):
   	repeat with R running through regions begin;
   		if the gatekeeper of R is the character, say "[R], ";
   	end repeat.

   Test me with "TEST denied/TEST expired-invite/TEST permit/TEST forbid/TEST fixit".
   Test denied with "stan, invite me / stan, invite me to sales".
   Test expired-invite with "i/bob, invite me to sales/visit p/i/visit s/i/visit h/i".
   Test permit with "i/bob, permit me/i/visit p/visit s/i/visit r".
   Test forbid with "i/visit bob/bob, forbid me/i/visit p/visit s/i".
   Test fixit with "go to break room/sw/find wrench/take wrench/go to break room/sw".

Regional Travel
===============

**Author:** Juhana Leinonen | **Version:** 2

Allows the player to travel between regions. Useful for example when the player
travels between large regions far apart from each other (e.g. cities), or for
traveling in vehicles and public transportation.

**Basic example:** East Side West Side

A bare minimum example of setting up Regional Travel

.. code-block:: inform7

   Use travel destination announcements.

   Chapter 1 - Setting up the world

   The West Bank is a region. The East Bank is a region.

   West end of the bridge is a room. Western Main Road is west of the West end of the bridge. Market Square is north of the Western Main Road. The Church is south of the Western Main Road.

   East end of the bridge is east of West end of the bridge. Eastern Main Road is east of the East end of the bridge. The Inn is southeast of the Eastern Main Road. The Blacksmith is south of the Eastern Main Road.

   West end of the bridge, Western Main Road, Market Square, and the Church are in the West Bank.
   East end of the bridge, Eastern Main Road, the Inn and the Blacksmith are in the East Bank.


   Chapter 2 - Travel entry points

   The travel entry point of the West Bank is the West end of the bridge. 
   The travel entry point of the East Bank is the East end of the bridge.     
   Understand "bank" as the West end of the bridge. Understand "bank" as the East end of the bridge.

   Test me with "e/e/s/travel to church/travel to foobar/travel to eastern main road/travel to blacksmith/travel to west bank/w/s/travel to blacksmith/e/travel to church/travel to east bank".

Relative Placement and Direction
================================

**Author:** Jeff Nyman | **Version:** 1.3

allowing relative directional movement as well as locationally relative
descriptions.

**Basic example:** A Relative Stroll Through a Park

.. code-block:: inform7

   Include Relative Placement and Direction by Jeff Nyman.

   Part - Locations

   Palace Gate is a room.
   Black Lion Gate is a room.
   Lancaster Gate is a room.

   Broad Walk is a room.
   Flower Walk is a room.
   Lancaster Walk is a room.

   Along Bayswater Road is a room.
   Round Pond is a room.
   Grassy Area is a room.

   Long Water is a room.
   Wading is a room.

   The default-facing of Wading is east.

   Part - Connections

   Broad Walk is north of Palace Gate.
   Flower Walk is east of Palace Gate.
   Lancaster Walk is north of Flower Walk.

   Black Lion Gate is north of Broad Walk.
   Lancaster Gate is north of Lancaster Walk.

   Along Bayswater Road is east of Black Lion Gate and west of Lancaster Gate.
   Along Bayswater Road is northeast of Broad Walk and northwest of Lancaster Walk.

   Round Pond is east of Broad Walk and west of Lancaster Walk.
   Round Pond is southeast of Black Lion Gate and southwest of Lancaster Gate.
   Round Pond is south of Along Bayswater Road.

   The Grassy Clearing is south of Round Pond, northeast of Palace Gate, and northwest of Flower Walk.
   The Grassy Clearing is southeast of Broad Walk and southwest of Lancaster Walk.

   Grassy Area is east of Lancaster Walk.
   Long Water is east of Grassy Area.

   A door called the tent door is down from Long Water and up from Sinkhole.
   The tent door is closed and openable.

   Wading is inside from Long Water.
   Wading is east of Long Water.

   Part - Setup of Status Line

   When play begins:
   	now the player is facing north.

   	Table of Fancy Status
   	left			central	right
   	""				""		"[top rose]"
   	" [location]"	""		"[middle rose]"
   	""				""		"[bottom rose]"

   Rule for constructing the status line:
   	fill the status bar with the Table of Fancy Status;
   	rule succeeds.

Scopability
===========

**Author:** Brady Garvin | **Version:** 2.0.220524

The ability to toggle objects' scopability; the parser does not acknowledge the
existence of unscopable objects, even if they are explicitly added to scope.

**Basic example:** The Visitor

An object that is present but unrevealed.

.. code-block:: inform7

   Include Scopability by Brady Garvin.

   Cavern is a room.
   The rocky debris is scenery.
   The alien artifact is an unscopable thing in the cavern.
   "It's embedded in the rock!"
   The description of the alien artifact is "It looks alien."

   Every turn when the alien artifact is in the location:
   	say "There's a faint humming coming from above."

   Instead of listening when the alien artifact is in the location:
   	say "Hmmmm hmmmm hmmmm.  Hm hm hm hm.  Hmmmm hm hm.  Hm.  Hm hmmmm.  Hm hmmmm hm."

   Instead of jumping when the alien artifact is in the location and the alien artifact is not scopable:
   	say "The jolt shakes [rocky debris] loose from the ceiling, revealing [an alien artifact]!";
   	now the rocky debris is in the location;
   	now the alien artifact is scopable;
   	now the alien artifact is not scenery.

   Test me with "z / listen / x artifact / jump / x artifact".

Scope Control
=============

**Author:** Ron Newcomb | **Version:** 2

Allows us to ask why the Deciding the Scope For Something activity is running,
so we can modify the scope only when we absolutely need to. Highly useful for
giving NPCs commands over telephones or while in darkness, creating 'can hear'
relations, or modifying how Inform parses the command line.

**Basic example:** "Asking for Directions"

A new internet acquaintance needs our help.

.. code-block:: inform7

   Include Scope Control by Ron Newcomb.

   Chapter 1 - The Emerald City

   The smell of coffee is a backdrop. A person can be lost in it.  Persuasion rule when the actor is lost in it: persuasion succeeds.

   Pike Place Market is west of Bauhaus Coffeeshop.  Bauhaus Coffeeshop is south of your apartment.  Yourself is in your apartment.

   Some salmon is in Pike Place Market.  A salmon dinner is in your apartment. 

   Coffee is everywhere.

   Jesse is a woman in Pike Place Market.  Jesse is lost in it.

   After looking for the first time: say "Your phone rings.  'Hey, it's Jesse.  How do I get to your place?'". 

   Chapter 2 - scope changes while we're on the phone

   Section 1 - the old way (for use without Scope Control by Ron Newcomb)

   After deciding the scope of the player when Jesse is lost in it:
   	place Jesse in scope.

   Section 2 - the new way (for use with Scope Control by Ron Newcomb)

   After deciding the scope of the player while parsing for persuasion and Jesse is lost in it: 
   	place Jesse in scope.

   Chapter 3 - Maze of Streets

   After anyone going: say "'OK.'". 

   Instead of Jesse going nowhere: say "'I think I'm lost.  Are you sure you gave me good directions?'"; now Jesse is in Pike Place Market; rule succeeds.

   After Jesse looking: say "'I think I'm at [the location of Jesse].'"

   A description of Jesse is "A brunette in a pullover hoodie and jeans, with legs made for striding up hills, Jesse has finally made it out to visit." 

   Test me with "jesse, look / jesse, e / jesse, s / examine jesse / * She's not in front of me, so I shouldn't be able to examine her right now. / jesse, look / jesse, e / jesse, n / jesse, look / examine jesse ".

Secret Doors
============

**Author:** Andrew Owen | **Version:** 1

Doors and switches that cannot be acted upon until they are discovered.

**Documented usage:**

.. code-block:: inform7

   The cave wall is scenery in the Big Cave.

Secret Doors
============

**Author:** Gavin Lambert | **Version:** 2

Doors and switches that cannot be acted upon until they are discovered.

**Basic example:** Simple Cave with Secret Door and Lever

This defines a simple two-room example similar to the above.

.. code-block:: inform7

   Include Secret Doors by Gavin Lambert.

   Big Cave is a room. "You're not sure how you ended up here, but you're surrounded on all sides by slightly damp rock.  Fortunately the walls seem to contain faintly glowing moss, so there's enough light to see by."
   The faintly glowing moss is scenery in the Big Cave.  "It glows just barely enough to make out your surroundings."

   Secret Passage is a room. "For being so close to a cave, this passage is surprisingly well built and is lit by standard electrical bulbs.  Unfortunately it also appears to be blocked by rubble not too far from the entrance; you can't seem to proceed any further."
   The rubble is scenery in the Secret Passage.  "It looks completely impassable."

   The passage door is an unopenable secret door.  "It's fairly unassuming.  You'd never have known it was there until it opened."
   It is west of the Big Cave and east of the Secret Passage.

   The hidden lever is a secret switch in the Big Cave.  "Nestled almost invisibly between two rocks in the cave wall.  [if the passage door is revealed]It has been pulled downwards.[otherwise]It points invitingly upwards.[end if]"

   The cave wall is scenery in the Big Cave.  "Nothing else more interesting presents itself.  Just more glowing moss."
   Understand "damp rock" or "rock" as the cave wall.

   Instead of going nowhere from the Big Cave:
   	say "The cave walls seem completely intact in that direction."

   Instead of searching or examining the cave wall for the first time:
   	now the lever is revealed;
   	say "As you examine the cave wall, in a gap between two rocks you discover a lever."
   	
   Instead of pulling or pushing the revealed lever:
   	if the passage door is revealed:
   		say "You don't have any desire to close the passage again.";
   	otherwise:
   		now the passage door is revealed;
   		now the passage door is open;
   		say "A secret door opens with a rumble, revealing a secret passage in the west wall!"

   Test me with "w / open door / pull lever / x wall / x lever / pull lever / x lever / w"

Title Case for Headings
=======================

**Author:** Nathanael Nerode | **Version:** 2.0.220529

Applies title case to room names printed as a heading or in the status line.
Creates the printing a heading activity for further customization. Tested with
Inform 10.1.0. Requires Undo Output Control by Nathanael Nerode to handle the
case of room name printing after UNDO.

**Basic example:** Meadow

The title is Meadow, the name is meadow

.. code-block:: inform7

   Include Undo Output Control by Nathanael Nerode.
   Include Title Case for Headings by Nathanael Nerode.

   A meadow is a room.  "This is a meadow."

   After deciding the scope of an object (called character):
   Place the location of the character in scope, but not its contents.

   test case with "take meadow / look / undo"

Universal Opening
=================

**Author:** Peter Orme | **Version:** 1.0.220524

**Basic example:** The secure piggy bank

A piggy bank that you can put things inside, even it it's closed and locked.
Including the key! In the test, you put the key in the locked piggy bank and use
"openall bank" to make it open.

.. code-block:: inform7

   Include Universal Opening by Peter Orme.

   Nursery is a room. 

   The piggy bank is a closed openable lockable container in the nursery. It is locked.

   The pink key unlocks the piggy bank. The player is carrying the pink key.

   instead of inserting something into the piggy bank:
   	say "You slip [the noun] through the slot on the piggy's back.";
   	now the noun is in the piggy bank.

   test me with "put key in bank / take key / open bank / openall bank / take key / close bank / open bank";
