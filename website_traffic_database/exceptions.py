"""Public exception hierarchy for the Website Traffic Database SDK."""

class WebsiteTrafficDatabaseError(Exception):
    """Base SDK error."""

class AuthenticationError(WebsiteTrafficDatabaseError):
    """The Apify token is missing or rejected."""

class ActorRunError(WebsiteTrafficDatabaseError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(WebsiteTrafficDatabaseError):
    """The client stopped waiting before the Actor completed."""
