#include <stdio.h>
#include <assert.h>

#include "code/binaryFileParser.hpp"

BinaryFileParser::BinaryFileParser(BufferedInputStream* stream) {
    file_stream = stream;
}

CodeObject* BinaryFileParser::parse() {
    int magic_number = file_stream->read_int();
    printf("magic number is 0x%x\n", magic_number);
    int moddate = file_stream->read_int();
    printf("moddate is 0x%x\n", moddate);

    char object_type = file_stream->read();

    if (object_type == 'c') {
        CodeObject* result = get_code_object();
        printf("parse OK!\n");
        return result;
    }

    return NULL;
}

CodeObject* BinaryFileParser::get_code_object() {
    return NULL;
}