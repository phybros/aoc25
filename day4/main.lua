grid = {}
timer = 0.0
totalremovals = 0
stepremovals = 0
running = false

function love.load()
    f = love.filesystem.read("input.txt")
    local y = 1

    for line in string.gmatch(f, "%S+") do
        local row = {}
        for i = 1, #line do
            local c = line:sub(i, i)
            table.insert(row, i, c)
        end
        table.insert(grid, y, row)
        y = y + 1
    end
end

function love.keypressed(key, scancode, isrepeat)
    if key == "space" then
        running = true
    end
end

local function processGrid()
    stepremovals = 0

    for y = 1, #grid do
        for x = 1, #grid[y] do
            if grid[y][x] == "@" then
                local neighs = 0

                if x - 1 >= 1 and grid[y][x - 1] == "@" then
                    neighs = neighs + 1
                end
                if x + 1 <= #grid[y] and grid[y][x + 1] == "@" then
                    neighs = neighs + 1
                end
                if y - 1 >= 1 and grid[y - 1][x] == "@" then
                    neighs = neighs + 1
                end
                if y + 1 <= #grid and grid[y + 1][x] == "@" then
                    neighs = neighs + 1
                end
                if x - 1 >= 1 and y - 1 >= 1 and grid[y - 1][x - 1] == "@" then
                    neighs = neighs + 1
                end
                if x + 1 <= #grid[y] and y + 1 <= #grid and grid[y + 1][x + 1] == "@" then
                    neighs = neighs + 1
                end
                if y + 1 <= #grid and x - 1 >= 1 and grid[y + 1][x - 1] == "@" then
                    neighs = neighs + 1
                end
                if y - 1 >= 1 and x + 1 <= #grid[y] and grid[y - 1][x + 1] == "@" then
                    neighs = neighs + 1
                end

                if neighs < 4 then
                    grid[y][x] = "x"
                    stepremovals = stepremovals + 1
                    totalremovals = totalremovals + 1
                end
            end
        end
    end
end

function love.update(dt)
    if not running then return end

    if timer > 0.1 then
        timer = 0.0

        processGrid()
    end

    timer = timer + dt
end

function love.draw()
    for y = 1, #grid do
        for x = 1, #grid[y] do
            if grid[y][x] == "@" then
                love.graphics.setColor(0.9, 0.9, 0.9, 1.0)
                love.graphics.circle("fill", x * 5, y * 5, 2)
            elseif grid[y][x] == "x" then
                love.graphics.setColor(0.1, 0.5, 0.1, 1.0)
                love.graphics.circle("fill", x * 5, y * 5, 2)
            else
                love.graphics.setColor(0.2, 0.2, 0.2, 1.0)
                love.graphics.rectangle("fill", x * 5 - 2, y * 5 - 2, 4, 4)
            end
        end
    end

    love.graphics.setColor(0.0, 0.1, 1.0, 0.75)
    love.graphics.rectangle("fill", 10, 650, 680, 40)

    if stepremovals == 0 and running then
        love.graphics.setColor(0.0, 1.0, 0.0, 1.0)
    else
        love.graphics.setColor(1.0, 1.0, 0.0, 1.0)
    end
    love.graphics.print("Total Removed: " .. totalremovals, 15, 650)

    love.graphics.setColor(1.0, 1.0, 0.0, 1.0)
    love.graphics.print("Removed This Step: " .. stepremovals, 15, 670)
end
