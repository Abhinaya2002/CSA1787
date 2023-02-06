female(pam).
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(peter).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).

parent(bob,pat).
parent(pat,jim).
parent(bob,peter).
parent(peter,jim).

mother(X,Y):- parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
uncle(X,Z):-brother(X,Y),parent(Y,Z).
Output
| ?- [family_ext].
compiling D:/TP Prolog/Sample_Codes/family_ext.pl for byte code...
D:/TP Prolog/Sample_Codes/family_ext.pl compiled, 27 lines read - 4646 bytes written, 10 ms

| ?- uncle(X,Y).

X = peter
Y = jim ? ;

no
| ?- grandparent(X,Y).

X = pam
Y = ann ? ;

X = pam
Y = pat ? ;

X = pam
Y = peter ? ;

X = tom
Y = ann ? ;

X = tom
Y = pat ? ;

X = tom
Y = peter ? ;

X = bob
Y = jim ? ;

X = bob
Y = jim ? ;

no
| ?- wife(X,Y).

X = pam
Y = tom ? ;

X = pat
Y = peter ? ;

(15 ms) no
| ?-
