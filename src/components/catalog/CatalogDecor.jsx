import { Box,Container,Typography } from "@mui/material"
export default function CatalogDecor(){
    return(<>
        {/* <Box>
        <img
          src="src\assets\img\header_catalog.jpg"
          alt="samsung"
          className="catalog_image"
        />
      </Box> */}
      <Container maxWidth="lg">
        <Box
          sx={{
            py: 8,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Typography variant="h2" sx={{ fontWeight: "700" }}>
            Laptop Catalog
          </Typography>
        </Box>
      </Container>
      </>
    )
}