from enum import Enum

class DevelopmentCardType(Enum):
    KNIGHT = 0
    VICTORY_POINT = 1
    MONOPOLY = 2
    ROAD_BUILDING = 3
    YEAR_OF_PLENTY = 4

class BuildingType(Enum):
    ROAD = 0
    SETTLEMENT = 1
    CITY = 2

class Border:
    def __init__(self):
        self.tiles : (Tile, Tile) = None

class Corner:
    def __init__(self):
        self.tiles : (Tile, Tile, Tile) = None

class DevelopmentCard:
    def __init__(self):
        self.card_type : DevelopmentCardType = None
        self.played : bool = false

class Building:
    def __init__(self):
        self.building_type : BuildingType = None
        self.is_border_location : bool = False
        self.border_location = Border
        self.corner_location = Corner

class Player:
    def __init__(self):
        self.score: int = 0
        self.development_cards: list[DevelopmentCard] = []
        self.structures: list[Building] = []
        self.longest_army: bool = False
        self.longest_road: bool = False

class Map:
    def __init__(self):
        self.tiles: list[Tile] = []
        self.borders: list[Border] = []
        self.corners: list[Corner] = []
        self.robber: Robber = None

class Deck:
    def __init__(self):
        self.development_cards: list[DevelopmentCard] = []
        self.brick = 0
        self.sheep = 0
        self.ore = 0
        self.weed = 0
        self.wood = 0

class State:
    def __init__(self, players: list[Player]):
        self.map: Map = Map()
        self.players: list[Player] = players
        self.deck: Deck = Deck()

state: State = State([Player(), Player()])
print(state.players[0].score)
