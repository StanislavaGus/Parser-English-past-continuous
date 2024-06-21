A program for constructing a context-free grammar of a subset of the English language in the Past continuous period. Grammar includes many terminal symbols - words, such as objects, place, time, prepositions, pronouns, etc., consisting
of words of the English language. Affirmative, exclamation, interrogative and negative sentences are implemented. 

The logic of statements hasn't checked.

***Grammar:***

  
     <sentence> ::= <affirmative sentence> | <negative sentence> | <interrogative sentence>
    
    <affirmative sentence> ::= <base> <complement> <punctuation>
    
    <negative sentence> ::= 
        <subject for was> was not <verb in Ving> <complement> <punctuation> |
        <subject for were> were not <verb in Ving> <complement> <punctuation>
    
    <interrogative sentence> ::= 
        was <subject for was> <verb in Ving> <complement> <question mark> |
        were <subject for were> <verb in Ving> <complement> <question mark>
    
    <base> ::= 
        <subject for was> was <verb in Ving> |
        <subject for were> were <verb in Ving>
    
    <complement> ::= 
        <circumstance of place> |
        <object> |
        <adverb> |
        <circumstance of time> |
        <object> <circumstance of place> |
        <adverb> <circumstance of place> |
        <object> <circumstance of time> |
        <adverb> <circumstance of time> |
        <object> <adverb> |
        <adverb> <circumstance of place> |
        <circumstance of time> <circumstance of place> |
        <object> <circumstance of time> <circumstance of place> |
        <adverb> <circumstance of time> <circumstance of place> |
        <object> <adverb> <circumstance of time> |
        <object> <adverb> <circumstance of place> |
        <object> <circumstance of time> <adverb> |
        <object> <circumstance of place> <adverb> |
        ""
    
    <subject for was> ::= I | he | she | it | John | <singular noun>
    
    <subject for were> ::= you | we | they | <plural noun>
    
    <verb in Ving> ::= <verb> ing
    
    <circumstance of place> ::= 
        <preposition place> <article> <place> |
        <preposition place> <place>
    
    <preposition place> ::= in | at | on | by | with | under | near | behind
    
    <place> ::= park | home | street | river | tree | lesson | dinner | meeting
    
    <circumstance of time> ::= <preposition time> <duration>
    
    <preposition time> ::= for | during | before | after
    
    <duration> ::= <measurement unit> | <length> <measurement unit>
    
    <length> ::= 3 | a | two | several | long | short
    
    <measurement unit> ::= weeks | month | year | days | hours | time | while
    
    <object> ::= <article> <noun>
    
    <verb> ::= go | read | sleep | watch | cook | run | walk
    
    <noun> ::= book | homework | keys | ball | news | project | meeting
    
    <article> ::= a | the | my
    
    <adverb> ::= quickly | slowly | quietly | loudly | suddenly | happily | sadly | angrily
    
    <punctuation> ::= <period> | <exclamation mark>
    
    <singular noun> ::= mom | dad | bird | cat | dog | person | friend | brother | sister
    
    <plural noun> ::= family | birds | cats | dogs | people | friends | brothers | sisters | siblings | neighbors
    
    <question mark> ::= ?
    <period> ::= .
    <exclamation mark> ::= !
