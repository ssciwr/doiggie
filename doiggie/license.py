from typing import Optional, Tuple
import dataclasses
import enum


class LicenseIdentifierScheme(enum.Enum):
    SPDX = "spdx"
    URL = "url"
    OTHER = "other"


@dataclasses.dataclass(frozen=True)
class LicenseIdentifier:
    scheme: LicenseIdentifierScheme
    value: str


class LicenseReferenceRole(enum.Enum):
    ICON = "icon"
    TEXT = "text"
    HOMEPAGE = "homepage"


@dataclasses.dataclass(frozen=True)
class LicenseReference:
    role: LicenseReferenceRole
    uri: str


@dataclasses.dataclass(frozen=True)
class License:
    name: str
    description: Optional[str] = None
    identifiers: Tuple[LicenseIdentifier, ...] = ()
    references: Tuple[LicenseReference, ...] = ()
    copyright: Optional[str] = None
