import cognee


async def store_contact_memory(email: str, name: str, fun_fact: str, context: str):
    memory_text = (
        f"Contact: {name} (email: {email}). "
        f"Fun fact: {fun_fact}. "
        f"Context from meeting: {context}"
    )
    await cognee.remember(memory_text)


async def recall_contact_context(email: str, name: str):
    results = await cognee.recall(
        query_text=f"What do I know about {name} with email {email}?"
    )
    return [r.text for r in results] if results else []