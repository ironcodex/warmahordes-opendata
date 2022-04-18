# Cards & Models

Out of all the game's concepts, the abstraction of cards and models has been the hardest
one to come up with so far as we use the word models in different contexts.

In general, models needs two things to be functional in the game:

1. A phisical representation, which are the miniatures we put our sweat, blood, and 
tears to assemble, paint, and later destroy during one of our attempts to play a game.

2. A card with rules, which describes the set of things a model can or cannot do.

![Crucible Guard Mechanik](https://scans.ironcodex.net/32dcae04-0652-34eb-ab91-f5c3fe1cd1ae)
Figure 1: Crucible Guard Mechanik

The Crucible Guard Mechanik, shown in Figure 1, has one miniature and one card, considering front and back, to represent the model in the game. This one-to-one
relationship is quite easy to understand and to word out as we are always in the
singuar: the model, the card.

Things start to get complicated when we move to a Warcaster:

![Syvestro 1 - Card 1](https://scans.ironcodex.net/76d6372b-ef7d-3c3a-96c4-cf523754a42d)
![Syvestro 1 - Card 2](https://scans.ironcodex.net/0d1444fd-86c2-39a4-9016-b34fdefbb056)
Figure 2: Aurum Adeptus Syvestro

In Syvestro 1's case, shown in Figure 2, we have one model with two cards. We could
then say that models can have one or more cards, creating a one-to-many relationship.

![Dragon's Breath Rocket](https://scans.ironcodex.net/2c9bf1bf-29c7-3d42-9fb2-29e930895775)
Figure 3: Dragon's Breath Rocket

But then we hit cases where multiple models are described in the same card, which is the
case of the Dragon's Breath Rocked shown on Figure 3. Now we have a single card, which
represents multiple models with different stats, weapons and rules.

![Gearhart 1 - Card 1](https://scans.ironcodex.net/9ba23fd9-b0e7-3762-8c91-478209bbf819)
![Gearhart 1 - Card 2](https://scans.ironcodex.net/134a0355-96cb-3366-9fe0-56a5010ce8ca)
![Gearhart 1 - Card 3](https://scans.ironcodex.net/6a00a4aa-2474-3dc7-bbd5-56ac36289a2b)
Figure 4: Marshal General Baldwin Gearhart & Mr. Clogg

In our last example, we have cases where two different models have their own cards, but
are only allowed in the game as a bundle, which is the case of Gearhart 1 and Clogg 1 that is composed of Gearhart himself and his assistant Mr Clogg, shown in Figure 4.
They have separate cards, but they only make sense together, as they share the same name
from the [card database][1] and the same cost, or in this
case the warjack points.

In the end, we decided to have the **Card** being the thing that
contains **Model(s)**, and the number of cards one or more models
can have is less relevant and can be represented as the number of
scans (card faces). Using this representation we can say that the
**Card** Crucible Guard Mechanik contains 2 scans (front and back) and a single **Model** Mechanik, while the **Card** Marshal General Baldwin Gearhart & Mr. Clogg contains 6 scans and two **Models**, Gearhart 1 and Clogg 1.

## The Card class

```mermaid
classDiagram

    class Card {
        ppid : int
        name : str
        scans : int
        point_cost : int | list[tuple[option: str, cost: int]] = 0
        battlegroup_points: int = 0
        field_allowance : int|str
        ...
    }
```

**ppid:** Unique identifier of the card in the [card database][1].

**name:** Name of the card in the [card database][1] and top of
each scan.

**scans:** Number of scans in a card, counts the number of card
faces, front and back, each counting as one.

E.g.:
1. Crucible Guard Mechanik -> 2 scans
2. Aurum Adeptus Syvestro -> 4 scans

**point_cost:** The point cost is tricky, cards will either contain
point costs or battlegroup allowance points, never both at the same
time. Point costs can be just the cost itself or a list of options
and their cost.

E.g.:
1. Crucible Guard Mechanik -> point_cost = 2
2. Dragon's Breath Rocket -> point_cost = [(option="Gunner & 2 Grunts", cost=4)]

**batlegroup_points:** The number of extra points allowed during the
list building for warjacks, warbeasts, and so on... for the caster's
battlegroup.

```mermaid
classDiagram

    class Card {
        ppid : int
        name : str
        models : list[Model]
        battlegroup_points: int
        point_cost : list[int|str]?
        field_allowance : int|str
        attachments: list[int]
        scans : int
    }

    class Model {
        name : str
        stats : ModelStats
        rules : list[Rule]
        weapons : list[Weapon]
        spells : list[Spell]
        feat: Rule
    }

    class ModelStats {
        spd : int
        str : int
        mat : int
        rat : int
        def : int
        arm : int
        cmd : int
        focus : int
        fury : int
        essence : int
        advantages : list[Advantage]
        base_size : BaseSize
    }

    class BaseSize {
        <<enumeration>>
        SMALL = 30
        MEDIUM = 40
        LARGE = 50
        EXTRA_LARGE = 80
        HUGE = 120
    }

    class Weapon {
        name : str
        type : str
        stats : WeaponStats
        qualities : list[WeaponQualities]
        rules : list[Rule]
    }

    class WeaponStats {
        rng: float
        pow: int
    }

    class MeleeWeaponStats {
        pns: bool
    }

    class RangeWeaponStats {
        rof: int
        aoe: int
        spray: bool
    }

    class Rule {
        name: str
        description: str
        choices: list[Rule]
    }

    Card *-- Model
    Model *-- ModelStats
    Model o-- Weapon
    Model o-- Rule
    ModelStats o-- BaseSize
    Weapon *-- WeaponStats
    Weapon o-- Rule
    WeaponStats <|-- MeleeWeaponStats
    WeaponStats <|-- RangeWeaponStats
    Rule o-- Rule
```

[1]: https://cards.privateerpress.com