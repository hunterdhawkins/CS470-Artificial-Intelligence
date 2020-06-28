%Hunter Hawkins-Stark
%Project #4 CS 470 AI
%Family Tree in Prolog
% This site had some very helpful rules that assisted me in getting started:
% https://www.101computing.net/prolog-family-tree/

%Define the men
man(liam).
man(noah).
man(william).
man(james).
man(oliver).
man(benjamin).
man(elijah).
man(lucas).
man(mason).
man(logan).

%Define the women
woman(emma).
woman(olivia).
woman(ava).
woman(isabella).
woman(sophia).
woman(charlotte).
woman(mia).
woman(amelia).
woman(harper).
women(evelyn).

%Who Liam is a parent to
parent(liam, noah).
parent(liam, olivia).
parent(liam, william).
parent(liam, ava).
parent(liam, james).
parent(liam, isabella).
parent(liam, oliver).
parent(liam, sophia).

%Who emma is a parent to
parent(emma, noah).
parent(emma, olivia).
parent(emma, william).
parent(emma, ava).
parent(emma, james).
parent(emma, isabella).
parent(emma, oliver).
parent(emma, sophia).

%Who noah is a parent to
parent(noah, benjamin).
parent(noah, charlotte).
parent(noah, elijah).
parent(noah, mia).

%Who Olivia is a parent to
parent(olivia, benjamin).
parent(olivia, charlotte).
parent(olivia, elijah).
parent(olivia, mia).

%william is parent to no one
%ava is parent to no one
%james is parent to no one
%isabella is parent to no one

%Who Oliver is a parent to
parent(oliver, lucas).
parent(oliver, amelia).
parent(oliver, mason).
parent(oliver, harper).

%Who Sophia is a parent to
parent(sophia, lucas).
parent(sophia, amelia).
parent(sophia, mason).
parent(sophia, harper).

%Who Elijah is a parent to
parent(elijah, logan).

%Who Mia is a parent to
parent(mia,logan).

%Who Lucas is a parent to
parent(lucas, evelyn).

%Who Amelia is a parent to
parent(amelia, evelyn).

grandparent(X,Y) :-
parent(Z,Y),
parent(X,Z).

grandfather(X,Y) :-
man(X),
grandparent(X,Y).

grandmother(X,Y) :-
woman(X),
grandparent(X,Y).

aunt(X,Y) :-
woman(X),
siblings(X,Z),
parent(Z,Y).

uncle(X,Y) :-
man(X),
siblings(X,Z),
parent(Z,Y).

mother(X,Y) :-
woman(X),
parent(X,Y).

father(X,Y) :-
man(X),
parent(X,Y).

child(X,Y) :-
parent(Y,X).

son(X,Y) :-
man(X),
child(X,Y).

daughter(X,Y) :-
woman(X),
child(X,Y).

siblings(X,Y) :-
parent(Z, X),
parent(Z, Y),
X\=Y.

brother(X,Y) :-
man(X),
siblings(X,Y).

sister(X,Y) :-
woman(X),
siblings(X,Y).

ancestor(X,Y) :-
descendant(Y,X).

descendant(X,Y) :-
parent(Y,X).

descendant(X,Y) :-
parent(Z,X),
descendant(Z,Y).

% X\=Y is equivalent to not (x = y)
related(X,Y) :-
ancestor(Z,X),
ancestor(Z,Y),
X\=Y.