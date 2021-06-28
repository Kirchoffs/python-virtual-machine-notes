#ifndef BINARY_FILE_PARSER
#define BINARY_FILE_PARSER

#include "util/bufferedInputStream.hpp"
#include "code/codeObject.hpp"

class BinaryFileParser {
private:
    BufferedInputStream* file_stream;
    int cur;
    CodeObject* get_code_object();

public:
    BinaryFileParser(BufferedInputStream* stream);

    CodeObject* parse();
};

#endif
