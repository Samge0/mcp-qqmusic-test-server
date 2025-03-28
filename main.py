import asyncio
from qqmusic_api import search
from mcp.server.fastmcp import FastMCP
import json

# Initialize FastMCP server
mcp = FastMCP("mcp-qqmusic-test-server")

@mcp.tool()
async def search_music(keyword: str, page: int = 1, num: int = 20):
    """
    Search for music tracks
    
    Args:
        keyword: Search keyword or phrase
        page: Page number for pagination (default: 1)
        num: Maximum number of results to return (default: 20)
        
    Returns:
        List of music tracks matching the search criteria
    """
    result = await search.search_by_type(keyword=keyword, page=page, num=num)
    
    # 提取指定字段
    # json.dumps(result, ensure_ascii=False) - 这行代码没有实际作用，因为结果没有被使用
    if isinstance(result, list):
        filtered_list = []
        for item in result:
            # 提取歌曲信息而不是专辑信息
            song_info = {
                "id": item.get("id"),
                "mid": item.get("mid"),
                "name": item.get("name"),
                "pmid": item.get("pmid", ""),
                "subtitle": item.get("subtitle", ""),
                "time_public": item.get("time_public", ""),
                "title": item.get("title", item.get("name", ""))
            }
            filtered_list.append(song_info)
    
    return filtered_list


if __name__ == "__main__":
    # print(asyncio.run(search_music("周杰伦")))
    mcp.run(transport='stdio')
