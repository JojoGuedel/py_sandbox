from enum import Enum

import Utils.Iota as Iota 


class TokenKind(Enum):
    Plus            = Iota.reset()
    Minus           = Iota.next()
    Star            = Iota.next()
    Slash           = Iota.next()
    Equal           = Iota.next()
    Pow             = Iota.next()
    LParen          = Iota.next()
    RParen          = Iota.next()

    Comma           = Iota.next()
    Space           = Iota.next()

    Number          = Iota.next()
    Literal         = Iota.next()
    FunctionName    = Iota.next()
    Invalid         = Iota.next()
    End             = Iota.next()