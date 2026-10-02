CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    source_file TEXT,
    uploaded_at TIMESTAMP DEFAULT now()
);

CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    document_id INT REFERENCES documents(id),
    content TEXT,
    embedding VECTOR(1536),
    chunk_index INT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops);