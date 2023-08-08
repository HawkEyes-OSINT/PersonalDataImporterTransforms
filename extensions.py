from maltego_trx.decorator_registry import TransformRegistry, TransformSet

# manual insert
setName = 'PersonalData'

registry = TransformRegistry(
    owner="HawkEyes",
    author="Hawk Dev",
    host_url="https://hawk-eyes.com",
    version="0.1.0",
    seed_ids=["demo"]
)

TransformSet = TransformSet(setName, f"{setName} Transforms")
