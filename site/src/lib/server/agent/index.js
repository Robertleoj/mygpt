import { ChatOpenAI } from "langchain/chat_models/openai";
import { 
    HumanChatMessage, 
    SystemChatMessage,  
    AIChatMessage
} from "langchain/schema";
import { OPENAI_API_KEY } from "$env/static/private";



function fixMessages(messages) {
    return messages.map(message => messageObjToSchema(message));
}

function messageObjToSchema(message) {
    switch (message.role) {
        case "human":
            return new HumanChatMessage(message.content);
        case "system":
            return new SystemChatMessage(message.content);
        case "assistant":
            return new AIChatMessage(message.content);
        default:
            throw new Error("Invalid message role");
    }
}


/*
messages is an array with messages of the format
{
    "role": "human" | "system" | "assistant",
    "content": "string"
}
*/
export async function getResponse(messages) {
    chat = new ChatOpenAI({
        temperature: 0,
        openAIApiKey: OPENAI_API_KEY
    });
    const fixedMessages = fixMessages(messages);
    const response = await chat.call(fixedMessages);

    return  {
        role: "assistant",
        content: response.text
    }
}


