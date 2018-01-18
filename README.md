# Assignment1 - Practice Designing Models

> * Participant name: Lauren Doocy
> * Project Title: Smart City Transportation Model

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. Our goal is to create a city with as low of a carbon footprint as possible. Many cities, communities, and campuses have already established goals of reaching a climate neutral state.

![Image of Smart City](images/smartcity.png)

Traffic congestion, espeically during rush hour, is a major problem in larger cities. While it is incovenient for individuals that commute to work, it also has negative effects on the environment. CO2 emissions produced by the operation of standard vehicles makes up for a majority of daily greenhouse gas (GHG) emissions in the United States. Among the environmental benefits that would be seen by reduced congestion, it would provide a safer environment to live in. Traffic accidents make up for numerous deaths nationwide and are are more likely to happen with more cars on the road.

This model is an agent based model where data is kept on the daily modes of transportation used by commuters. In an attempt to lower GHG emissions, it will attempt to lower the number of single passenger cars on the road. Less single passenger cars may mean more commuters are using public transportation, more people are using alternate routes, or more people are carpooling. The one thing that these things have in common is a reduction of cars on the road, and the reduction of average time a car spends on the road.

For the purposes of making reasonable change, we will focus on users commuting to and from work and school. This is the most consistent transportation by users. A majority of users perform this action 5 times a week. Where as transportation to the grocery store, gym, mall, etc do not happen as regularily.

Through this simulation we will gain a better understanding of what drives our users to use certain modes of transportation. While convenience is a giant playing card in what drives agents to do what they do, heavy traffic congestion at rush hour is not convenient for anyone. Thus, through incentives, widened variety of safe transportation options, among other things that drive people, we seek to decrease congestion on roadways during rush hour and therefore lowering GHG emissions generated.

## Requirements

User transportation preferences will only change when something changes. This system will implement changes to the current transporation options one at a time and view how it changes transportation preferences of the users. These changes will be things such as adding more bus stops, implementing a transit train system, repaving and creating safer bike paths and walk ways, and insentive programs for carpooling commuters. With each implementation user preferences will be re-evaluated and the number of single passenger cars on the road will be assessed.

## Smart City Transportation Model

This model makes an effort at indentifying the transportation of choice by residents of a city. When preferences are identified, we can further aim to reduce the number of solo drivers on the road.

* [**Object Diagram**](model/object_diagram.md) - provides details of the various types of intercity transportation and the different components involved
* [**Class Diagram**](model/class_diagram.md) - provides details of the attributes and functions of different transportation options within a city
* [**User case**](model/agent_usecase_diagram.md) - provides details of the transportation preferences of various users

## Smart City Transportation Simulation

This is the rough plan for the [**Smart City Transportation Model**](model/README.md) simulation. Much of this type of progress will be made after understanding what motivates specific types of people to use certain modes of transportation to get to work.


## Smart City Transportation Model

Here [**we provide an overview**](code/README.md) of a Smart City Transportation Model.
