def lookup(collection_key_child, key_mother):
    collection_child, key_child = collection_key_child.split(':')

    mongo_lookup_syntax = [{
        "$lookup": {
            "from": collection_child,  # foreign collection name
            "foreignField": key_child,  # foreign key name
            "localField": key_mother,  # local collection key name
            "as": key_mother,
        }
    }]
    return mongo_lookup_syntax


def filter_deleted(keys_father, key_mother):
    filter_syntax = [
        {
            "$match": {
                "deleted": False
            }
        },
        {
            "$project": {
                **dict(zip(keys_father, [1] * len(keys_father))),
                "deleted": 1,  # yapf: disable
                key_mother: {
                    "$filter": {
                        "input": "$" + key_mother,
                        "as": "child",
                        "cond": {
                            "$eq": ["$$child.deleted", False]
                        },
                    },
                }
            }
        }
    ]
    return filter_syntax


def prune_fields(keys_father, key_mother, keys_child):
    prune_child = [{
        "$project": {
            **dict(zip(keys_father, [1] * len(keys_father))), key_mother:
            dict(zip(keys_child, [1] * len(keys_child)))
        }
    }]
    return prune_child


def filter_deleted_tag():
    filter_syntax = [{"$match": {"deleted": False}}]
    return filter_syntax


def prune_fields_tag():
    prune_tag = [{"$project": {"tag": 1}}]
    return prune_tag

def hide_password(user):
    user['password'] = user['password'][:30] + '*' * 30 + '...'
    return user