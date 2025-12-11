#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_map>

struct Server
{
    std::string id;
    std::vector<std::string> connections;
};

void log(const std::string &msg, const std::string &end = "\n")
{
    std::cout << msg << end;
}

// there's probably a smarter way to do this
std::vector<std::string> getConnectionsById(const std::vector<Server> &servers, const std::string &id)
{
    for (const auto &server : servers)
    {
        if (server.id == id)
        {
            return server.connections;
        }
    }
    return std::vector<std::string>();
}

// this is so gross looking but works great
std::unordered_map<std::string, std::unordered_map<std::string, long long>> memo;

long long countPaths(
    const std::vector<Server> &servers,
    const std::string &from,
    const std::string &to)
{
    if (from == to)
        return 1;

    if (memo[from].count(to))
    {
        return memo[from][to];
    }

    long long count = 0;
    for (const auto &conn : getConnectionsById(servers, from))
    {
        count += countPaths(servers, conn, to);
    }

    memo[from][to] = count;
    return count;
}

int main(void)
{
    std::vector<Server> allServers;

    std::ifstream ifs("input.txt");
    if (!ifs)
    {
        std::cerr << "Failed to open input.txt" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(ifs, line))
    {
        std::istringstream partsstream(line);
        std::string part;
        std::string id;
        std::vector<std::string> parts;

        bool first = true;

        // new trick learned!
        // reads whitespace-separated strings from the string stream one at a time
        while (partsstream >> part)
        {
            if (first)
            {
                id = part.substr(0, part.size() - 1); // remove colon
                first = false;
            }
            else
            {
                parts.push_back(part);
            }
        }

        allServers.emplace_back(id, parts);
    }

    long long fftdac = countPaths(allServers, "svr", "fft") * countPaths(allServers, "fft", "dac") * countPaths(allServers, "dac", "out");
    long long dacfft = countPaths(allServers, "svr", "dac") * countPaths(allServers, "dac", "fft") * countPaths(allServers, "fft", "out");
    long long answer = fftdac + dacfft;

    log("Total Paths from svr -> out (with fft and dac): ", "");
    log(std::to_string(answer));

    return 0;
}
