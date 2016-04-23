from aiohttp import web


class Handler(web.View):
    async def paging(self, page, count, per_page):
        page_count = int(count/per_page) + int(bool(count % per_page))

        if page > page_count:
            page = page_count
        if page < 1:
            page = 1
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        if page < page_count:
            next_page = page + 1
        else:
            next_page = None

        return page_count, prev_page, page, next_page
