from typing import Union

from eth_hash.auto import keccak as keccak_256
from hashlib import blake2b as BLAKE2B

from .conversions import (
    to_bytes,
)


def keccak(primitive: Union[bytes, int, bool]=None, hexstr: str=None, text: str=None) -> bytes:
    return keccak_256(to_bytes(primitive, hexstr, text))


def blake2b(primitive: Union[bytes, int, bool]=None, hexstr: str=None, text: str=None, digest_size=64) -> bytes:
    return BLAKE2B(to_bytes(primitive, hexstr, text), digest_size=digest_size).digest()


def blake2b_raw(primitive: Union[bytes, int, bool]=None, hexstr: str=None, text: str=None, digest_size=64) -> bytes:
    return BLAKE2B(to_bytes(primitive, hexstr, text), digest_size=digest_size)
