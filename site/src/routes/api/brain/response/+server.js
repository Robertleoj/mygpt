import { json } from "@sveltejs/kit";
import { getResponse } from "$lib/server/agent";

export async function POST({ request }) {
    const { messages } = await request.json();

    const response = await getResponse(messages);

    return json({ response });
}