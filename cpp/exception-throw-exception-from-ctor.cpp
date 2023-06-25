/*
Throwing exceptions from C++ constructors

An exception should be thrown from a C++ constructor whenever an object cannot be properly constructed or initialized.
Since there is no way to recover from failed object construction, an exception should be thrown in such cases.

Constructors should also throw C++ exceptions to signal any input parameters received outside of allowed values or range
of values.

Since C++ constructors do not have a return type, it is not possible to use return codes. Therefore, the best practice
is for constructors to throw an exception to signal failure.

The throw statement can be used to throw an C++ exception and exit the constructor code.
*/

#include <fstream>
#include <iostream>
#include <map>
#include <memory>

// See https://stackoverflow.com/questions/48759799/how-to-replace-the-home-directory-with-a-tilde-linux
#include <wordexp.h>

// bool writeData(std::shared_ptr<std::ofstream>& stream, const std::string& data, const std::string& path,
//                const bool flush) {
//     try {
//         stream->write(data.c_str(), data.size());
//         if (flush) {
//             stream->flush();
//         }
//     } catch (const std::system_error& e) {
//         std::cerr << "Failed writing " << data.size() << " bytes to " << path << " due to " << e.what() << "("
//                   << e.code() << ")";
//         return false;
//     }
//     return true;
// }

void writeData(std::shared_ptr<std::ofstream>& stream, const std::string& data, const std::string& path,
               const bool flush) {
    try {
        stream->write(data.c_str(), data.size());
        if (flush) {
            stream->flush();
        }
    } catch (const std::system_error& e) {
        std::cerr << "Failed writing " << data.size() << " bytes to " << path << " due to " << e.what() << "("
                  << e.code() << ")" << std::endl;
        throw e;
    }
}

// put all the horrible bits into a function
std::string wordexp(const std::string& var, int flags = 0) {
    wordexp_t p;
    std::string expansion;
    if (!wordexp(var.c_str(), &p, flags)) {
        if (p.we_wordc && p.we_wordv[0]) expansion = p.we_wordv[0];
        wordfree(&p);
    }
    return std::move(expansion);
}

class Stream {
  public:
    Stream(const std::map<std::string, std::string>& stream_paths);

  private:
    std::map<std::string, std::shared_ptr<std::ofstream>> _streams;
};

Stream::Stream(const std::map<std::string, std::string>& stream_paths) {
    for (const auto& kv : stream_paths) {
        std::shared_ptr<std::ofstream> os(new std::ofstream());
        os->exceptions(std::ifstream::failbit | std::ifstream::badbit);
        std::string filename = kv.second;
#if TILDE_EXPANSION
        filename = wordexp(filename);
#endif
        std::cout << "Opening " << filename << std::endl;
        try {
            // just open in write mode, it ll erase all the contents
            os->open(filename);
        } catch (const std::system_error& e) {
            std::cerr << "Failed opening " << filename << " duo to " << e.what() << "(" << e.code() << ")" << std::endl;
            throw e;  // re-throw it for the broken stream
        }
        writeData(os, "header line", filename, true);
        _streams.insert(std::make_pair(kv.first, os));
    }
}

int main() {
    std::map<std::string, std::string> paths = {
      {"A", "~/tmp.log"},
    };

    Stream stream(paths);
    return 0;
}

/*
$ g++ exception-throw-exception-from-ctor.cpp
$ ./a.out
Opening ~/tmp.log
Failed opening ~/tmp.log duo to basic_ios::clear: iostream error(iostream:1)
terminate called after throwing an instance of 'std::system_error'
  what():  basic_ios::clear: iostream error
Aborted

$ g++ exception-throw-exception-from-ctor.cpp -DTILDE_EXPANSION=1

$ ./a.out
Opening /home/immjolnir/tmp.log

$ cat /home/immjolnir/tmp.log
header line
*/
